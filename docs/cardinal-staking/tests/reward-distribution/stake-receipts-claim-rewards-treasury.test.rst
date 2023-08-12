tests/reward-distribution/stake-receipts-claim-rewards-treasury.test.ts
=======================================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { findAta } from "@cardinal/common";
import { BN } from "@coral-xyz/anchor";
import { getAccount } from "@solana/spl-token";
import type { Keypair } from "@solana/web3.js";
import { PublicKey, Transaction } from "@solana/web3.js";

import {
  createStakeEntryAndStakeMint,
  createStakePool,
  initializeRewardEntry,
  stake,
  unstake,
} from "../../src";
import { RewardDistributorKind } from "../../src/programs/rewardDistributor";
import {
  getRewardDistributor,
  getRewardEntry,
} from "../../src/programs/rewardDistributor/accounts";
import {
  findRewardDistributorId,
  findRewardEntryId,
} from "../../src/programs/rewardDistributor/pda";
import { withInitRewardDistributor } from "../../src/programs/rewardDistributor/transaction";
import { ReceiptType } from "../../src/programs/stakePool";
import { getStakeEntry } from "../../src/programs/stakePool/accounts";
import { findStakeEntryIdFromMint } from "../../src/programs/stakePool/utils";
import {
  createMasterEdition,
  createMint,
  delay,
  executeTransaction,
} from "../utils";
import type { CardinalProvider } from "../workspace";
import { getProvider } from "../workspace";

describe("Stake and claim rewards from treasury", () => {
  const maxSupply = 100;

  let provider: CardinalProvider;
  let stakePoolId: PublicKey;
  let originalMintTokenAccountId: PublicKey;
  let originalMintId: PublicKey;
  let rewardMintId: PublicKey;
  let stakeMintKeypair: Keypair | undefined;

  beforeAll(async () => {
    provider = await getProvider();
    provider = await getProvider();
    // original mint
    [originalMintTokenAccountId, originalMintId] = await createMasterEdition(
      provider.connection,
      provider.wallet
    );

    // reward mint
    [, rewardMintId] = await createMint(provider.connection, provider.wallet, {
      amount: maxSupply,
    });
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

  it("Create Reward Distributor", async () => {
    const transaction = new Transaction();

    await withInitRewardDistributor(
      transaction,
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        rewardMintId: rewardMintId,
        kind: RewardDistributorKind.Treasury,
        maxSupply: new BN(maxSupply),
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const rewardDistributorId = findRewardDistributorId(stakePoolId);
    const rewardDistributorData = await getRewardDistributor(
      provider.connection,
      rewardDistributorId
    );

    expect(rewardDistributorData.parsed.rewardMint.toString()).toEqual(
      rewardMintId.toString()
    );

    expect(rewardDistributorData.parsed.rewardMint.toString()).toEqual(
      rewardMintId.toString()
    );
  });

  it("Create Reward Entry", async () => {
    const rewardDistributorId = findRewardDistributorId(stakePoolId);
    const stakeEntryId = await findStakeEntryIdFromMint(
      provider.connection,
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId
    );

    const transaction = await initializeRewardEntry(
      provider.connection,
      provider.wallet,
      {
        originalMintId: originalMintId,
        stakePoolId: stakePoolId,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const rewardEntryId = findRewardEntryId(rewardDistributorId, stakeEntryId);

    const rewardEntryData = await getRewardEntry(
      provider.connection,
      rewardEntryId
    );

    expect(rewardEntryData.parsed.rewardDistributor.toString()).toEqual(
      rewardDistributorId.toString()
    );

    expect(rewardEntryData.parsed.stakeEntry.toString()).toEqual(
      stakeEntryId.toString()
    );
  });

  it("Init stake entry and mint", async () => {
    let transaction: Transaction;

    [transaction, , stakeMintKeypair] = await createStakeEntryAndStakeMint(
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        originalMintId: originalMintId,
      }
    );
    await executeTransaction(
      provider.connection,
      transaction,
      provider.wallet,
      {
        signers: stakeMintKeypair ? [stakeMintKeypair] : [],
      }
    );

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
    expect(stakeEntryData.parsed.stakeMint?.toString()).toEqual(
      stakeMintKeypair?.publicKey.toString()
    );
  });

  it("Stake", async () => {
    const transaction = await stake(provider.connection, provider.wallet, {
      stakePoolId: stakePoolId,
      originalMintId: originalMintId,
      userOriginalMintTokenAccountId: originalMintTokenAccountId,
      receiptType: ReceiptType.Receipt,
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

    const stakeEntryOriginalMintTokenAccountId = await findAta(
      originalMintId,
      stakeEntryData.pubkey,
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
    expect(Number(checkUserOriginalTokenAccount.amount)).toEqual(0);

    const checkStakeEntryOriginalMintTokenAccount = await getAccount(
      provider.connection,
      stakeEntryOriginalMintTokenAccountId
    );
    expect(Number(checkStakeEntryOriginalMintTokenAccount.amount)).toEqual(1);

    if (!stakeMintKeypair) {
      throw new Error("stakeMintKeypair is undefined");
    }

    const stakeEntryId = await findStakeEntryIdFromMint(
      provider.connection,
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId
    );

    const userReceiptMintTokenAccountId = await findAta(
      stakeMintKeypair.publicKey,
      provider.wallet.publicKey,
      true
    );

    const stakeEntryReceiptMintTokenAccountId = await findAta(
      stakeMintKeypair.publicKey,
      stakeEntryId,
      true
    );

    const checkUserReceiptMintTokenAccount = await getAccount(
      provider.connection,
      userReceiptMintTokenAccountId
    );
    expect(Number(checkUserReceiptMintTokenAccount.amount)).toEqual(1);

    const checkStakeEntryReceiptMintTokenAccount = await getAccount(
      provider.connection,
      stakeEntryReceiptMintTokenAccountId
    );
    expect(Number(checkStakeEntryReceiptMintTokenAccount.amount)).toEqual(0);
  });

  it("Unstake", async () => {
    await delay(2000);
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

    if (!stakeMintKeypair) {
      throw new Error("stakeMintKeypair is undefined");
    }

    const userOriginalMintTokenAccountId = await findAta(
      originalMintId,
      provider.wallet.publicKey,
      true
    );

    const userReceiptMintTokenAccountId = await findAta(
      stakeMintKeypair.publicKey,
      provider.wallet.publicKey,
      true
    );

    const stakeEntryOriginalMintTokenAccountId = await findAta(
      originalMintId,
      stakeEntryData.pubkey,
      true
    );

    const stakeEntryReceiptMintTokenAccountId = await findAta(
      stakeMintKeypair.publicKey,
      stakeEntryData.pubkey,
      true
    );

    const userRewardMintTokenAccountId = await findAta(
      rewardMintId,
      provider.wallet.publicKey,
      true
    );

    const checkUserReceiptMintTokenAccount = await getAccount(
      provider.connection,
      userReceiptMintTokenAccountId
    );
    expect(Number(checkUserReceiptMintTokenAccount.amount)).toEqual(0);

    const checkStakeEntryReceiptMintTokenAccount = await getAccount(
      provider.connection,
      stakeEntryReceiptMintTokenAccountId
    );
    expect(Number(checkStakeEntryReceiptMintTokenAccount.amount)).toEqual(1);

    const checkUserOriginalTokenAccount = await getAccount(
      provider.connection,
      userOriginalMintTokenAccountId
    );
    expect(Number(checkUserOriginalTokenAccount.amount)).toEqual(1);

    const checkStakeEntryOriginalMintTokenAccount = await getAccount(
      provider.connection,
      stakeEntryOriginalMintTokenAccountId
    );
    expect(Number(checkStakeEntryOriginalMintTokenAccount.amount)).toEqual(0);

    const checkUserRewardTokenAccount = await getAccount(
      provider.connection,
      userRewardMintTokenAccountId
    );
    expect(Number(checkUserRewardTokenAccount.amount)).toBeGreaterThan(1);
  });
});


