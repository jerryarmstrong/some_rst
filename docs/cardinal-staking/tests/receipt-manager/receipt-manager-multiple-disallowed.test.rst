tests/receipt-manager/receipt-manager-multiple-disallowed.test.ts
=================================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { findAta, tryGetAccount, withWrapSol } from "@cardinal/common";
import { getPaymentManager } from "@cardinal/payment-manager/dist/cjs/accounts";
import { findPaymentManagerAddress } from "@cardinal/payment-manager/dist/cjs/pda";
import { withInit } from "@cardinal/payment-manager/dist/cjs/transaction";
import { BN, Wallet } from "@coral-xyz/anchor";
import { getAccount } from "@solana/spl-token";
import {
  Keypair,
  LAMPORTS_PER_SOL,
  PublicKey,
  Transaction,
} from "@solana/web3.js";

import { createStakeEntry, createStakePool, stake } from "../../src";
import { RECEIPT_MANAGER_PAYMENT_MANAGER_NAME } from "../../src/programs/receiptManager";
import {
  getReceiptEntry,
  getReceiptManager,
  getRewardReceipt,
} from "../../src/programs/receiptManager/accounts";
import {
  findReceiptEntryId,
  findReceiptManagerId,
  findRewardReceiptId,
} from "../../src/programs/receiptManager/pda";
import {
  withClaimRewardReceipt,
  withInitReceiptEntry,
  withInitReceiptManager,
  withInitRewardReceipt,
  withSetRewardReceiptAllowed,
  withUpdateReceiptManager,
} from "../../src/programs/receiptManager/transaction";
import { ReceiptType } from "../../src/programs/stakePool";
import { getStakeEntry } from "../../src/programs/stakePool/accounts";
import { findStakeEntryId } from "../../src/programs/stakePool/pda";
import { findStakeEntryIdFromMint } from "../../src/programs/stakePool/utils";
import {
  createMasterEdition,
  executeTransaction,
  newAccountWithLamports,
} from "../utils";
import type { CardinalProvider } from "../workspace";
import { getProvider } from "../workspace";

describe("Receipt manages multiple with disallowlist", () => {
  let provider: CardinalProvider;
  let originalMintTokenAccountId: PublicKey;
  let originalMintId: PublicKey;
  let stakePoolId: PublicKey;

  const receiptManagerName1 = `mgr-${Math.random()}`;
  const receiptManagerName2 = `mgr-${Math.random()}`;
  const requiredStakeSeconds = new BN(0);
  const stakeSecondsToUse = new BN(1);
  const requiresAuthorization = false;

  const MAKER_FEE = 0;
  const TAKER_FEE = 0;
  const feeCollector = Keypair.generate();
  const paymentRecipient = Keypair.generate();
  const paymentMint = new PublicKey(
    "So11111111111111111111111111111111111111112"
  );

  beforeAll(async () => {
    provider = await getProvider();
    // original mint
    const mintAuthority = await newAccountWithLamports(provider.connection);
    [originalMintTokenAccountId, originalMintId] = await createMasterEdition(
      provider.connection,
      new Wallet(mintAuthority),
      { target: provider.wallet.publicKey }
    );

    const transaction = new Transaction();
    await withWrapSol(
      transaction,
      provider.connection,
      provider.wallet,
      LAMPORTS_PER_SOL
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);
  });

  it("Create payment manager", async () => {
    const transaction = new Transaction();

    const [paymentManagerId] = await findPaymentManagerAddress(
      RECEIPT_MANAGER_PAYMENT_MANAGER_NAME
    );
    const checkIfPaymentManagerExists = await tryGetAccount(() =>
      getPaymentManager(provider.connection, paymentManagerId)
    );
    if (!checkIfPaymentManagerExists) {
      await withInit(
        transaction,
        provider.connection,
        provider.wallet,
        RECEIPT_MANAGER_PAYMENT_MANAGER_NAME,
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

    const paymentManagerData = await getPaymentManager(
      provider.connection,
      paymentManagerId
    );
    expect(paymentManagerData.parsed.name).toEqual(
      RECEIPT_MANAGER_PAYMENT_MANAGER_NAME
    );
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

  it("Create Reward Receipt Manager", async () => {
    const transaction = new Transaction();
    const [, receiptManagerId] = await withInitReceiptManager(
      transaction,
      provider.connection,
      provider.wallet,
      {
        name: receiptManagerName1,
        stakePoolId: stakePoolId,
        authority: provider.wallet.publicKey,
        requiredStakeSeconds: requiredStakeSeconds,
        stakeSecondsToUse: stakeSecondsToUse,
        paymentMint: paymentMint,
        paymentRecipientId: paymentRecipient.publicKey,
        requiresAuthorization: requiresAuthorization,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const receiptManagerData = await getReceiptManager(
      provider.connection,
      receiptManagerId
    );
    const [payamentManagerId] = await findPaymentManagerAddress(
      RECEIPT_MANAGER_PAYMENT_MANAGER_NAME
    );
    expect(receiptManagerData.parsed.name.toString()).toEqual(
      receiptManagerName1
    );
    expect(receiptManagerData.parsed.paymentManager.toString()).toEqual(
      payamentManagerId.toString()
    );
    expect(receiptManagerData.parsed.authority.toString()).toEqual(
      provider.wallet.publicKey.toString()
    );
    expect(receiptManagerData.parsed.paymentMint.toString()).toEqual(
      paymentMint.toString()
    );
    expect(receiptManagerData.parsed.stakePool.toString()).toEqual(
      stakePoolId.toString()
    );
    expect(receiptManagerData.parsed.requiredStakeSeconds.toString()).toEqual(
      requiredStakeSeconds.toString()
    );
    expect(receiptManagerData.parsed.stakeSecondsToUse.toString()).toEqual(
      stakeSecondsToUse.toString()
    );
    expect(receiptManagerData.parsed.requiresAuthorization.toString()).toEqual(
      requiresAuthorization.toString()
    );
  });

  it("Create Reward Receipt Manager", async () => {
    const transaction = new Transaction();
    const [, receiptManagerId] = await withInitReceiptManager(
      transaction,
      provider.connection,
      provider.wallet,
      {
        name: receiptManagerName2,
        stakePoolId: stakePoolId,
        authority: provider.wallet.publicKey,
        requiredStakeSeconds: requiredStakeSeconds,
        stakeSecondsToUse: stakeSecondsToUse,
        paymentMint: paymentMint,
        paymentRecipientId: paymentRecipient.publicKey,
        requiresAuthorization: requiresAuthorization,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const receiptManagerData = await getReceiptManager(
      provider.connection,
      receiptManagerId
    );
    const [payamentManagerId] = await findPaymentManagerAddress(
      RECEIPT_MANAGER_PAYMENT_MANAGER_NAME
    );
    expect(receiptManagerData.parsed.name.toString()).toEqual(
      receiptManagerName2
    );
    expect(receiptManagerData.parsed.paymentManager.toString()).toEqual(
      payamentManagerId.toString()
    );
    expect(receiptManagerData.parsed.authority.toString()).toEqual(
      provider.wallet.publicKey.toString()
    );
    expect(receiptManagerData.parsed.paymentMint.toString()).toEqual(
      paymentMint.toString()
    );
    expect(receiptManagerData.parsed.stakePool.toString()).toEqual(
      stakePoolId.toString()
    );
    expect(receiptManagerData.parsed.requiredStakeSeconds.toString()).toEqual(
      requiredStakeSeconds.toString()
    );
    expect(receiptManagerData.parsed.stakeSecondsToUse.toString()).toEqual(
      stakeSecondsToUse.toString()
    );
    expect(receiptManagerData.parsed.requiresAuthorization.toString()).toEqual(
      requiresAuthorization.toString()
    );
  });

  it("Init stake entry for pool", async () => {
    const [transaction, _] = await createStakeEntry(
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        originalMintId: originalMintId,
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

    expect(stakeEntryData.parsed.originalMint.toString()).toEqual(
      originalMintId.toString()
    );
    expect(stakeEntryData.parsed.pool.toString()).toEqual(
      stakePoolId.toString()
    );
    expect(stakeEntryData.parsed.stakeMint).toEqual(null);
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

  it("Init Receipt Entry", async () => {
    const transaction = new Transaction();

    const stakeEntryId = findStakeEntryId(
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId,
      false
    );
    const [, receiptEntryId] = await withInitReceiptEntry(
      transaction,
      provider.connection,
      provider.wallet,
      {
        stakeEntryId: stakeEntryId,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const receiptEntryData = await getReceiptEntry(
      provider.connection,
      receiptEntryId
    );
    expect(receiptEntryData.parsed.stakeEntry.toString()).toEqual(
      receiptEntryData.parsed.stakeEntry.toString()
    );
    expect(receiptEntryData.parsed.usedStakeSeconds.toNumber()).toEqual(0);
  });

  it("Init Reward Receipt, first receipt manager", async () => {
    const transaction = new Transaction();

    const receiptManagerId = findReceiptManagerId(
      stakePoolId,
      receiptManagerName1
    );
    const stakeEntryId = findStakeEntryId(
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId,
      false
    );

    const receiptEntryId = findReceiptEntryId(stakeEntryId);
    const [, rewardReceiptId] = await withInitRewardReceipt(
      transaction,
      provider.connection,
      provider.wallet,
      {
        receiptManagerId: receiptManagerId,
        receiptEntryId: receiptEntryId,
        stakeEntryId: stakeEntryId,
        payer: provider.wallet.publicKey,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const rewardReceiptData = await getRewardReceipt(
      provider.connection,
      rewardReceiptId
    );
    expect(rewardReceiptData.parsed.allowed).toBeTruthy();
    expect(rewardReceiptData.parsed.target.toString()).toEqual(
      PublicKey.default.toString()
    );
    expect(rewardReceiptData.parsed.receiptEntry.toString()).toEqual(
      receiptEntryId.toString()
    );
    expect(rewardReceiptData.parsed.receiptManager.toString()).toEqual(
      receiptManagerId.toString()
    );
  });

  it("Init Reward Receipt, second receipt manager", async () => {
    const transaction = new Transaction();

    const receiptManagerId = findReceiptManagerId(
      stakePoolId,
      receiptManagerName2
    );
    const stakeEntryId = findStakeEntryId(
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId,
      false
    );

    const receiptEntryId = findReceiptEntryId(stakeEntryId);
    const [, rewardReceiptId] = await withInitRewardReceipt(
      transaction,
      provider.connection,
      provider.wallet,
      {
        receiptManagerId: receiptManagerId,
        receiptEntryId: receiptEntryId,
        stakeEntryId: stakeEntryId,
        payer: provider.wallet.publicKey,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const rewardReceiptData = await getRewardReceipt(
      provider.connection,
      rewardReceiptId
    );
    expect(rewardReceiptData.parsed.allowed).toBeTruthy();
    expect(rewardReceiptData.parsed.target.toString()).toEqual(
      PublicKey.default.toString()
    );
    expect(rewardReceiptData.parsed.receiptEntry.toString()).toEqual(
      receiptEntryId.toString()
    );
    expect(rewardReceiptData.parsed.receiptManager.toString()).toEqual(
      receiptManagerId.toString()
    );
  });

  it("Set requires authorization to true for second receipt manager", async () => {
    const transaction = new Transaction();

    const receiptManagerId = findReceiptManagerId(
      stakePoolId,
      receiptManagerName2
    );
    const beforeReceiptManagerData = await getReceiptManager(
      provider.connection,
      receiptManagerId
    );
    expect(beforeReceiptManagerData.parsed.requiresAuthorization).toBeFalsy();

    await withUpdateReceiptManager(
      transaction,
      provider.connection,
      provider.wallet,
      {
        name: receiptManagerName2,
        stakePoolId: stakePoolId,
        authority: beforeReceiptManagerData.parsed.authority,
        requiredStakeSeconds:
          beforeReceiptManagerData.parsed.requiredStakeSeconds,
        stakeSecondsToUse: beforeReceiptManagerData.parsed.stakeSecondsToUse,
        paymentMint: beforeReceiptManagerData.parsed.paymentMint,
        paymentRecipientId: beforeReceiptManagerData.parsed.paymentRecipient,
        requiresAuthorization: true,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const afterReceiptManagerData = await getReceiptManager(
      provider.connection,
      receiptManagerId
    );
    expect(afterReceiptManagerData.parsed.requiresAuthorization).toBeTruthy();
  });

  it("Set reward receipt auth to false, second receipt manager", async () => {
    const transaction = new Transaction();

    const stakeEntryId = findStakeEntryId(
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId,
      false
    );
    const receiptManagerId = findReceiptManagerId(
      stakePoolId,
      receiptManagerName2
    );

    const receiptEntryId = findReceiptEntryId(stakeEntryId);
    const receiptId = findRewardReceiptId(receiptManagerId, receiptEntryId);
    const beforeReceiptData = await getRewardReceipt(
      provider.connection,
      receiptId
    );
    expect(beforeReceiptData.parsed.allowed).toBeTruthy();

    await withSetRewardReceiptAllowed(
      transaction,
      provider.connection,
      provider.wallet,
      {
        auth: false,
        receiptManagerId: receiptManagerId,
        rewardReceiptId: receiptId,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const afterReceiptData = await getRewardReceipt(
      provider.connection,
      receiptId
    );
    expect(afterReceiptData.parsed.allowed).toBeFalsy();
  });

  it("Claim Reward Receipt, first receipt manager", async () => {
    const stakeEntryId = findStakeEntryId(
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId,
      false
    );
    const receiptEntryId = findReceiptEntryId(stakeEntryId);
    const paymentTokenAccountId = await findAta(
      paymentMint,
      paymentRecipient.publicKey,
      true
    );
    let beforeBalance = 0;
    try {
      beforeBalance = Number(
        (await getAccount(provider.connection, paymentTokenAccountId)).amount
      );
    } catch (e) {
      beforeBalance = 0;
    }

    const transaction = new Transaction();
    const [, rewardReceiptId] = await withClaimRewardReceipt(
      transaction,
      provider.connection,
      provider.wallet,
      {
        receiptManagerName: receiptManagerName1,
        stakePoolId: stakePoolId,
        stakeEntryId: stakeEntryId,
        claimer: provider.wallet.publicKey,
        payer: provider.wallet.publicKey,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const receiptManagerId = findReceiptManagerId(
      stakePoolId,
      receiptManagerName1
    );

    const checkRewardReceiptData = await tryGetAccount(() =>
      getRewardReceipt(provider.connection, rewardReceiptId)
    );
    expect(checkRewardReceiptData).not.toBeNull();
    expect(checkRewardReceiptData?.parsed.target.toString()).toEqual(
      provider.wallet.publicKey.toString()
    );
    expect(checkRewardReceiptData?.parsed.receiptEntry.toString()).toEqual(
      receiptEntryId.toString()
    );
    expect(checkRewardReceiptData?.parsed.receiptManager.toString()).toEqual(
      receiptManagerId.toString()
    );

    const paymentTokenAccountData = await getAccount(
      provider.connection,
      paymentTokenAccountId
    );
    expect(paymentTokenAccountData.amount.toString()).toEqual(
      (beforeBalance + 2 * 10 ** 6).toString()
    );

    const receiptEntryData = await getReceiptEntry(
      provider.connection,
      receiptEntryId
    );
    expect(receiptEntryData.parsed.usedStakeSeconds.toNumber()).toEqual(
      stakeSecondsToUse.toNumber()
    );
  });

  it("Fail to Claim Reward Receipt, second receipt manager", async () => {
    const stakeEntryId = findStakeEntryId(
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId,
      false
    );

    const transaction = new Transaction();
    await withClaimRewardReceipt(
      transaction,
      provider.connection,
      provider.wallet,
      {
        receiptManagerName: receiptManagerName2,
        stakePoolId: stakePoolId,
        stakeEntryId: stakeEntryId,
        claimer: provider.wallet.publicKey,
        payer: provider.wallet.publicKey,
      }
    );

    await expect(
      executeTransaction(provider.connection, transaction, provider.wallet, {
        silent: true,
      })
    ).rejects.toThrow();
  });
});


