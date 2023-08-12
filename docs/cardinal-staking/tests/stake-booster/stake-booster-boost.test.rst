tests/stake-booster/stake-booster-boost.test.ts
===============================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { findAta } from "@cardinal/common";
import { withInit } from "@cardinal/payment-manager/dist/cjs/transaction";
import { getAccount, getAssociatedTokenAddressSync } from "@solana/spl-token";
import { Keypair, PublicKey, Transaction } from "@solana/web3.js";
import { BN } from "bn.js";

import { createStakePool, stake, unstake } from "../../src";
import {
  ReceiptType,
  STAKE_BOOSTER_PAYMENT_MANAGER,
  STAKE_BOOSTER_PAYMENT_MANAGER_NAME,
} from "../../src/programs/stakePool";
import { getStakeEntry } from "../../src/programs/stakePool/accounts";
import {
  withBoostStakeEntry,
  withInitStakeBooster,
  withUpdateTotalStakeSeconds,
} from "../../src/programs/stakePool/transaction";
import { findStakeEntryIdFromMint } from "../../src/programs/stakePool/utils";
import {
  createMasterEditionTx,
  createMint,
  delay,
  executeTransaction,
} from "../utils";
import type { CardinalProvider } from "../workspace";
import { getProvider } from "../workspace";

describe("Stake booster boost", () => {
  let provider: CardinalProvider;
  let stakePoolId: PublicKey;
  let originalMintTokenAccountId: PublicKey;
  let originalMintId: PublicKey;
  const feeCollector = Keypair.generate();

  let paymentMintTokenAccount: PublicKey;
  let paymentMintId: PublicKey;
  const STAKE_BOOSTER_PAYMENT_AMOUNT = new BN(2);
  const BOOST_SECONDS = new BN(10);
  const SECONDS_TO_BOOST = new BN(3);
  const PAYMENT_SUPPLY = new BN(100);
  const MAKER_FEE = 50;
  const TAKER_FEE = 0;

  beforeAll(async () => {
    provider = await getProvider();
    const mintKeypair = Keypair.generate();
    originalMintId = mintKeypair.publicKey;
    originalMintTokenAccountId = getAssociatedTokenAddressSync(
      originalMintId,
      provider.wallet.publicKey
    );

    // master edition
    const transaction = await createMasterEditionTx(
      provider.connection,
      mintKeypair.publicKey,
      provider.wallet.publicKey
    );
    await executeTransaction(
      provider.connection,
      transaction,
      provider.wallet,
      { signers: [mintKeypair] }
    );

    [paymentMintTokenAccount, paymentMintId] = await createMint(
      provider.connection,
      provider.wallet,
      { amount: PAYMENT_SUPPLY.toNumber() }
    );

    // payment mint
    const stakeBoostPaymentManager = await provider.connection.getAccountInfo(
      STAKE_BOOSTER_PAYMENT_MANAGER
    );
    if (!stakeBoostPaymentManager) {
      // create payment manager
      const transaction = new Transaction();
      await withInit(
        transaction,
        provider.connection,
        provider.wallet,
        STAKE_BOOSTER_PAYMENT_MANAGER_NAME,
        feeCollector.publicKey,
        MAKER_FEE,
        TAKER_FEE,
        false
      );
      await executeTransaction(
        provider.connection,
        transaction,
        provider.wallet
      );
    }
  });

  it("Create Pool", async () => {
    let transaction: Transaction;
    [transaction, stakePoolId] = await createStakePool(
      provider.connection,
      provider.wallet,
      {}
    );

    await executeTransaction(provider.connection, transaction, provider.wallet);
  });

  it("Create booster", async () => {
    const transaction = await withInitStakeBooster(
      new Transaction(),
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        paymentAmount: STAKE_BOOSTER_PAYMENT_AMOUNT,
        paymentMint: paymentMintId,
        boostSeconds: BOOST_SECONDS,
        startTimeSeconds: Date.now() / 1000,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);
  });

  it("Stake", async () => {
    const transaction = await stake(provider.connection, provider.wallet, {
      stakePoolId: stakePoolId,
      originalMintId: originalMintId,
      userOriginalMintTokenAccountId: originalMintTokenAccountId,
      receiptType: ReceiptType.Original,
    });
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const stakeEntryData = await getStakeEntry(
      provider.connection,
      await findStakeEntryIdFromMint(
        provider.connection,
        provider.wallet.publicKey,
        stakePoolId,
        originalMintId
      )
    );

    const userOriginalMintTokenAccountId = await findAta(
      originalMintId,
      provider.wallet.publicKey,
      true
    );

    expect(stakeEntryData.parsed.lastStakedAt.toNumber()).toBeGreaterThan(0);
    expect(stakeEntryData.parsed.lastStaker.toString()).toEqual(
      provider.wallet.publicKey.toString()
    );

    const checkUserOriginalTokenAccount = await getAccount(
      provider.connection,
      userOriginalMintTokenAccountId
    );
    expect(Number(checkUserOriginalTokenAccount.amount)).toEqual(1);
    expect(checkUserOriginalTokenAccount.isFrozen).toEqual(true);
  });

  it("Update", async () => {
    await delay(1000);
    const stakeEntryId = await findStakeEntryIdFromMint(
      provider.connection,
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId
    );
    const oldStakeEntryData = await getStakeEntry(
      provider.connection,
      stakeEntryId
    );
    const transaction = new Transaction();
    await withUpdateTotalStakeSeconds(
      transaction,
      provider.connection,
      provider.wallet,
      {
        stakeEntryId: stakeEntryId,
        lastStaker: provider.wallet.publicKey,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const stakeEntryData = await getStakeEntry(
      provider.connection,
      stakeEntryId
    );
    expect(stakeEntryData.parsed.lastUpdatedAt).not.toEqual(null);
    expect(oldStakeEntryData.parsed.lastUpdatedAt).not.toEqual(null);
    expect(stakeEntryData.parsed.lastUpdatedAt?.toNumber()).toBeGreaterThan(
      oldStakeEntryData.parsed.lastUpdatedAt?.toNumber() ?? 0
    );
    expect(stakeEntryData.parsed.lastStaker.toString()).toEqual(
      provider.wallet.publicKey.toString()
    );
    expect(stakeEntryData.parsed.totalStakeSeconds.toNumber()).toBeGreaterThan(
      oldStakeEntryData.parsed.totalStakeSeconds.toNumber()
    );

    const userOriginalMintTokenAccountId = await findAta(
      originalMintId,
      provider.wallet.publicKey,
      true
    );
    const checkUserOriginalTokenAccount = await getAccount(
      provider.connection,
      userOriginalMintTokenAccountId
    );
    expect(Number(checkUserOriginalTokenAccount.amount)).toEqual(1);
    expect(checkUserOriginalTokenAccount.isFrozen).toEqual(true);
  });

  it("Boost", async () => {
    await delay(5000);
    const stakeEntryId = await findStakeEntryIdFromMint(
      provider.connection,
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId
    );
    const oldStakeEntryData = await getStakeEntry(
      provider.connection,
      stakeEntryId
    );
    const transaction = await withBoostStakeEntry(
      new Transaction(),
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        stakeEntryId: stakeEntryId,
        originalMintId: originalMintId,
        payerTokenAccount: paymentMintTokenAccount,
        secondsToBoost: SECONDS_TO_BOOST,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const stakeEntryData = await getStakeEntry(
      provider.connection,
      await findStakeEntryIdFromMint(
        provider.connection,
        provider.wallet.publicKey,
        stakePoolId,
        originalMintId
      )
    );
    expect(stakeEntryData.parsed.lastStaker.toString()).toEqual(
      provider.wallet.publicKey.toString()
    );
    expect(oldStakeEntryData.parsed.lastStakedAt.toNumber()).toEqual(
      stakeEntryData.parsed.lastStakedAt.toNumber()
    );
    expect(stakeEntryData.parsed.totalStakeSeconds.toNumber()).toEqual(
      oldStakeEntryData.parsed.totalStakeSeconds
        .add(SECONDS_TO_BOOST)
        .toNumber()
    );
    const userOriginalMintTokenAccountId = await findAta(
      originalMintId,
      provider.wallet.publicKey,
      true
    );
    const checkUserOriginalTokenAccount = await getAccount(
      provider.connection,
      userOriginalMintTokenAccountId
    );
    expect(Number(checkUserOriginalTokenAccount.amount)).toEqual(1);
    expect(checkUserOriginalTokenAccount.isFrozen).toEqual(true);

    const checkPaymentMintTokenAccount = await getAccount(
      provider.connection,
      paymentMintTokenAccount
    );
    expect(Number(checkPaymentMintTokenAccount.amount)).toEqual(
      PAYMENT_SUPPLY.sub(
        SECONDS_TO_BOOST.mul(STAKE_BOOSTER_PAYMENT_AMOUNT).div(BOOST_SECONDS)
      ).toNumber()
    );
  });

  it("Unstake", async () => {
    await delay(2000);
    const stakeEntryId = await findStakeEntryIdFromMint(
      provider.connection,
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId
    );
    const oldStakeEntryData = await getStakeEntry(
      provider.connection,
      stakeEntryId
    );

    const transaction = await unstake(provider.connection, provider.wallet, {
      stakePoolId: stakePoolId,
      originalMintId: originalMintId,
    });
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const stakeEntryData = await getStakeEntry(
      provider.connection,
      await findStakeEntryIdFromMint(
        provider.connection,
        provider.wallet.publicKey,
        stakePoolId,
        originalMintId
      )
    );
    expect(stakeEntryData.parsed.lastStaker.toString()).toEqual(
      PublicKey.default.toString()
    );
    expect(stakeEntryData.parsed.lastStakedAt.toNumber()).toBeGreaterThan(0);
    expect(stakeEntryData.parsed.totalStakeSeconds.toNumber()).toBeGreaterThan(
      oldStakeEntryData.parsed.totalStakeSeconds.toNumber()
    );
    const userOriginalMintTokenAccountId = await findAta(
      originalMintId,
      provider.wallet.publicKey,
      true
    );
    const checkUserOriginalTokenAccount = await getAccount(
      provider.connection,
      userOriginalMintTokenAccountId
    );
    expect(Number(checkUserOriginalTokenAccount.amount)).toEqual(1);
    expect(checkUserOriginalTokenAccount.isFrozen).toEqual(false);
  });

  it("Fail boost while unstaked", async () => {
    const stakeEntryId = await findStakeEntryIdFromMint(
      provider.connection,
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId
    );
    const transaction = await withBoostStakeEntry(
      new Transaction(),
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        originalMintId: originalMintId,
        stakeEntryId: stakeEntryId,
        payerTokenAccount: paymentMintTokenAccount,
        secondsToBoost: SECONDS_TO_BOOST,
      }
    );
    await expect(
      executeTransaction(provider.connection, transaction, provider.wallet, {
        silent: true,
      })
    ).rejects.toThrow();
  });

  it("Fail boost too far", async () => {
    const stakeEntryId = await findStakeEntryIdFromMint(
      provider.connection,
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId
    );
    const transaction = await withBoostStakeEntry(
      new Transaction(),
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        stakeEntryId: stakeEntryId,
        originalMintId: originalMintId,
        payerTokenAccount: paymentMintTokenAccount,
        secondsToBoost: SECONDS_TO_BOOST.mul(new BN(10)),
      }
    );
    await expect(
      executeTransaction(provider.connection, transaction, provider.wallet, {
        silent: true,
      })
    ).rejects.toThrow();
  });
});


