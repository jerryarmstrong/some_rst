tests/reward-distribution/max-reward-seconds.test.ts
====================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { executeTransactions, findAta } from "@cardinal/common";
import { BN } from "@coral-xyz/anchor";
import { getAccount } from "@solana/spl-token";
import { PublicKey, Transaction } from "@solana/web3.js";

import {
  claimRewards,
  createStakePool,
  rewardDistributor,
  stake,
  unstake,
} from "../../src";
import { RewardDistributorKind } from "../../src/programs/rewardDistributor";
import { getRewardDistributor } from "../../src/programs/rewardDistributor/accounts";
import { findRewardDistributorId } from "../../src/programs/rewardDistributor/pda";
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

describe("Stake and claim rewards up to max reward seconds", () => {
  let provider: CardinalProvider;
  let originalMintTokenAccountId: PublicKey;
  let originalMintId: PublicKey;
  let rewardMintId: PublicKey;
  let stakePoolId: PublicKey;

  const maxSupply = 100;
  const maxRewardSeconds = 1;

  beforeAll(async () => {
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
    await rewardDistributor.transaction.withInitRewardDistributor(
      transaction,
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        rewardMintId: rewardMintId,
        kind: RewardDistributorKind.Treasury,
        maxSupply: new BN(maxSupply),
        rewardAmount: new BN(1),
        rewardDurationSeconds: new BN(1),
        maxRewardSecondsReceived: new BN(maxRewardSeconds),
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

    const checkRewardDistributorTokenAccount = await getAccount(
      provider.connection,
      await findAta(rewardMintId, rewardDistributorId, true)
    );
    expect(Number(checkRewardDistributorTokenAccount.amount)).toEqual(
      maxSupply
    );
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

    expect(stakeEntryData.parsed.lastStakedAt.toNumber()).toBeGreaterThan(0);
    expect(stakeEntryData.parsed.lastStaker.toString()).toEqual(
      provider.wallet.publicKey.toString()
    );

    const checkUserOriginalTokenAccount = await getAccount(
      provider.connection,
      await findAta(originalMintId, provider.wallet.publicKey, true)
    );
    expect(Number(checkUserOriginalTokenAccount.amount)).toEqual(1);
    expect(checkUserOriginalTokenAccount.isFrozen).toEqual(true);
  });

  it("Claim Rewards", async () => {
    await delay(3000);
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

    const transactions = await claimRewards(
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        stakeEntryIds: [stakeEntryId],
      }
    );
    await executeTransactions(
      provider.connection,
      transactions,
      provider.wallet,
      {
        errorHandler: () => {
          throw Error("Error occurred");
        },
      }
    );

    const newStakeEntryData = await getStakeEntry(
      provider.connection,
      stakeEntryId
    );
    expect(newStakeEntryData.parsed.lastStaker.toString()).toEqual(
      provider.wallet.publicKey.toString()
    );
    expect(newStakeEntryData.parsed.lastUpdatedAt).not.toEqual(null);
    expect(oldStakeEntryData.parsed.lastUpdatedAt).not.toEqual(null);
    expect(newStakeEntryData.parsed.lastUpdatedAt?.toNumber()).toBeGreaterThan(
      oldStakeEntryData.parsed.lastStakedAt.toNumber()
    );
    expect(
      newStakeEntryData.parsed.totalStakeSeconds.toNumber()
    ).toBeGreaterThan(oldStakeEntryData.parsed.totalStakeSeconds.toNumber());

    const userRewardMintTokenAccountId = await findAta(
      rewardMintId,
      provider.wallet.publicKey,
      true
    );

    const checkUserRewardTokenAccount = await getAccount(
      provider.connection,
      userRewardMintTokenAccountId
    );
    expect(Number(checkUserRewardTokenAccount.amount)).toEqual(
      maxRewardSeconds
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

  it("Claim Rewards again", async () => {
    await delay(2000);
    const stakeEntryId = await findStakeEntryIdFromMint(
      provider.connection,
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId
    );
    const transaction = await claimRewards(
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        stakeEntryIds: [stakeEntryId],
      }
    );
    await expect(
      executeTransactions(provider.connection, transaction, provider.wallet, {
        errorHandler: () => {
          throw Error("Error occurred");
        },
      })
    ).rejects.toThrow();
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
      stakeEntryId
    );
    expect(stakeEntryData.parsed.lastStaker.toString()).toEqual(
      PublicKey.default.toString()
    );
    expect(stakeEntryData.parsed.lastStakedAt.toNumber()).toBeGreaterThan(0);

    const newStakeEntryData = await getStakeEntry(
      provider.connection,
      stakeEntryId
    );
    expect(newStakeEntryData.parsed.lastStaker.toString()).toEqual(
      PublicKey.default.toString()
    );
    expect(
      newStakeEntryData.parsed.totalStakeSeconds.toNumber()
    ).toBeGreaterThan(oldStakeEntryData.parsed.totalStakeSeconds.toNumber());
    const checkUserOriginalTokenAccount = await getAccount(
      provider.connection,
      await findAta(originalMintId, provider.wallet.publicKey, true)
    );
    expect(Number(checkUserOriginalTokenAccount.amount)).toEqual(1);
    expect(checkUserOriginalTokenAccount.isFrozen).toEqual(false);

    const stakeEntryOriginalMintTokenAccountId = await findAta(
      originalMintId,
      stakeEntryData.pubkey,
      true
    );

    const userRewardMintTokenAccountId = await findAta(
      rewardMintId,
      provider.wallet.publicKey,
      true
    );

    const checkStakeEntryOriginalMintTokenAccount = await getAccount(
      provider.connection,
      stakeEntryOriginalMintTokenAccountId
    );
    expect(Number(checkStakeEntryOriginalMintTokenAccount.amount)).toEqual(0);

    const checkUserRewardTokenAccount = await getAccount(
      provider.connection,
      userRewardMintTokenAccountId
    );
    expect(Number(checkUserRewardTokenAccount.amount)).toEqual(
      maxRewardSeconds
    );
  });
});


