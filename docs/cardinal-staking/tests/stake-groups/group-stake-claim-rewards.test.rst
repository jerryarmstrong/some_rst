tests/stake-groups/group-stake-claim-rewards.test.ts
====================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { findAta } from "@cardinal/common";
import { Wallet } from "@coral-xyz/anchor";
import { getAccount } from "@solana/spl-token";
import { PublicKey, Transaction } from "@solana/web3.js";

import {
  claimGroupRewards,
  closeGroupEntry,
  createGroupEntry,
  createGroupRewardDistributor,
  createStakePool,
  initializeRewardEntry,
  initUngrouping,
  stake,
  unstake,
} from "../../src";
import {
  getGroupRewardDistributor,
  getGroupRewardEntry,
} from "../../src/programs/groupRewardDistributor/accounts";
import { findGroupRewardEntryId } from "../../src/programs/groupRewardDistributor/pda";
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
import {
  getGroupStakeEntry,
  getStakeEntry,
} from "../../src/programs/stakePool/accounts";
import { findStakeEntryIdFromMint } from "../../src/programs/stakePool/utils";
import {
  createMasterEdition,
  createMint,
  delay,
  executeTransaction,
  newAccountWithLamports,
} from "../utils";
import type { CardinalProvider } from "../workspace";
import { getProvider } from "../workspace";

// reward distributor with mint youre are not authority

describe("Group stake and claim rewards", () => {
  let provider: CardinalProvider;
  let originalMintTokenAccountId: PublicKey;
  let originalMintId: PublicKey;
  let originalMint2TokenAccountId: PublicKey;
  let originalMintId2: PublicKey;
  let rewardMintId: PublicKey;
  let groupRewardMintId: PublicKey;
  let stakePoolId: PublicKey;
  let groupRewardDistributorId: PublicKey;
  let groupStakeEntryId: PublicKey;

  beforeAll(async () => {
    provider = await getProvider();

    // original mint
    const mintAuthority = await newAccountWithLamports(provider.connection);
    [originalMintTokenAccountId, originalMintId] = await createMasterEdition(
      provider.connection,
      new Wallet(mintAuthority),
      { target: provider.wallet.publicKey }
    );

    // original mint 2
    [originalMint2TokenAccountId, originalMintId2] = await createMasterEdition(
      provider.connection,
      new Wallet(mintAuthority),
      { target: provider.wallet.publicKey }
    );

    // reward mint
    [, rewardMintId] = await createMint(provider.connection, provider.wallet);
    [, groupRewardMintId] = await createMint(
      provider.connection,
      provider.wallet
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

  it("Create Reward Distributor", async () => {
    const transaction = new Transaction();

    await withInitRewardDistributor(
      transaction,
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        rewardMintId: rewardMintId,
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

  it("Create Group Reward Distributor", async () => {
    const [transaction, rewardDistributorId] =
      await createGroupRewardDistributor(provider.connection, provider.wallet, {
        authorizedPools: [stakePoolId],
        rewardMintId: groupRewardMintId,
      });
    groupRewardDistributorId = rewardDistributorId;
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const rewardDistributorData = await getGroupRewardDistributor(
      provider.connection,
      rewardDistributorId
    );

    expect(rewardDistributorData.parsed.rewardMint.toString()).toEqual(
      groupRewardMintId.toString()
    );

    expect(rewardDistributorData.parsed.rewardMint.toString()).toEqual(
      groupRewardMintId.toString()
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
        stakePoolId: stakePoolId,
        originalMintId: originalMintId,
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

  it("Create Reward Entry 2", async () => {
    const rewardDistributorId = findRewardDistributorId(stakePoolId);
    const stakeEntryId = await findStakeEntryIdFromMint(
      provider.connection,
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId2
    );

    const transaction = await initializeRewardEntry(
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        originalMintId: originalMintId2,
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

  it("Stake2", async () => {
    const transaction = await stake(provider.connection, provider.wallet, {
      stakePoolId: stakePoolId,
      originalMintId: originalMintId2,
      userOriginalMintTokenAccountId: originalMint2TokenAccountId,
      receiptType: ReceiptType.Original,
    });
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const stakeEntryData = await getStakeEntry(
      provider.connection,
      await findStakeEntryIdFromMint(
        provider.connection,
        provider.wallet.publicKey,
        stakePoolId,
        originalMintId2
      )
    );

    const userOriginalMintTokenAccountId = await findAta(
      originalMintId2,
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

  it("Create Group Stake Entry", async () => {
    const stakeEntryId = await findStakeEntryIdFromMint(
      provider.connection,
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId
    );

    const stakeEntryId2 = await findStakeEntryIdFromMint(
      provider.connection,
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId2
    );

    const [transaction, groupEntryId] = await createGroupEntry(
      provider.connection,
      provider.wallet,
      {
        stakeEntryIds: [stakeEntryId, stakeEntryId2],
      }
    );
    groupStakeEntryId = groupEntryId;
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const groupStakeEntryData = await getGroupStakeEntry(
      provider.connection,
      groupEntryId
    );

    expect(groupStakeEntryData.parsed.stakeEntries.length).toEqual(2);

    for (const id of [stakeEntryId, stakeEntryId2]) {
      const stakeEntry = await getStakeEntry(provider.connection, id);
      expect(stakeEntry.parsed.grouped).toEqual(true);
    }
  });

  it("Claim Group Rewards", async () => {
    await delay(2000);
    const stakeEntryId = await findStakeEntryIdFromMint(
      provider.connection,
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId
    );
    const stakeEntryId2 = await findStakeEntryIdFromMint(
      provider.connection,
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId2
    );
    const oldGroupStakeEntryData = await getGroupStakeEntry(
      provider.connection,
      groupStakeEntryId
    );
    const groupRewardEntryId = findGroupRewardEntryId(
      groupRewardDistributorId,
      groupStakeEntryId
    );

    const [transaction] = await claimGroupRewards(
      provider.connection,
      provider.wallet,
      {
        groupRewardDistributorId,
        groupEntryId: groupStakeEntryId,
        stakeEntryIds: [stakeEntryId, stakeEntryId2],
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const newGroupStakeEntryData = await getGroupStakeEntry(
      provider.connection,
      groupStakeEntryId
    );
    const groupRewardEntryData = await getGroupRewardEntry(
      provider.connection,
      groupRewardEntryId
    );

    expect(newGroupStakeEntryData.parsed.changedAt.toNumber()).toEqual(
      oldGroupStakeEntryData.parsed.changedAt.toNumber()
    );
    expect(
      groupRewardEntryData.parsed.rewardSecondsReceived.toNumber()
    ).toBeGreaterThan(1);

    const userGroupRewardMintTokenAccountId = await findAta(
      groupRewardMintId,
      provider.wallet.publicKey,
      true
    );
    const checkUserRewardTokenAccount = await getAccount(
      provider.connection,
      userGroupRewardMintTokenAccountId
    );
    expect(Number(checkUserRewardTokenAccount.amount)).toBeGreaterThan(1);
  });

  it("Start cooldown period", async () => {
    const [transaction] = await initUngrouping(
      provider.connection,
      provider.wallet,
      {
        groupEntryId: groupStakeEntryId,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const groupStakeEntryData = await getGroupStakeEntry(
      provider.connection,
      groupStakeEntryId
    );

    expect(groupStakeEntryData.parsed.groupCooldownStartSeconds).not.toBeNull();
  });

  it("Close group", async () => {
    const stakeEntryId = await findStakeEntryIdFromMint(
      provider.connection,
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId
    );

    const stakeEntryId2 = await findStakeEntryIdFromMint(
      provider.connection,
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId2
    );

    const [transaction] = await closeGroupEntry(
      provider.connection,
      provider.wallet,
      {
        groupEntryId: groupStakeEntryId,
        groupRewardDistributorId,
        stakeEntryIds: [stakeEntryId, stakeEntryId2],
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const userGroupRewardMintTokenAccountId = await findAta(
      groupRewardMintId,
      provider.wallet.publicKey,
      true
    );
    const checkUserRewardTokenAccount = await getAccount(
      provider.connection,
      userGroupRewardMintTokenAccountId
    );
    expect(Number(checkUserRewardTokenAccount.amount)).toBeGreaterThan(1);

    for (const id of [stakeEntryId, stakeEntryId2]) {
      const stakeEntry = await getStakeEntry(provider.connection, id);
      expect(stakeEntry.parsed.grouped).toEqual(false);
    }
  });

  it("Unstake", async () => {
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
    expect(Number(checkUserRewardTokenAccount.amount)).toBeGreaterThan(1);
  });

  it("Unstake2", async () => {
    const transaction = await unstake(provider.connection, provider.wallet, {
      stakePoolId: stakePoolId,
      originalMintId: originalMintId2,
    });
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const stakeEntryData = await getStakeEntry(
      provider.connection,
      await findStakeEntryIdFromMint(
        provider.connection,
        provider.wallet.publicKey,
        stakePoolId,
        originalMintId2
      )
    );
    expect(stakeEntryData.parsed.lastStaker.toString()).toEqual(
      PublicKey.default.toString()
    );
    expect(stakeEntryData.parsed.lastStakedAt.toNumber()).toBeGreaterThan(0);

    const userOriginalMintTokenAccountId = await findAta(
      originalMintId2,
      provider.wallet.publicKey,
      true
    );
    const checkUserOriginalTokenAccount = await getAccount(
      provider.connection,
      userOriginalMintTokenAccountId
    );
    expect(Number(checkUserOriginalTokenAccount.amount)).toEqual(1);
    expect(checkUserOriginalTokenAccount.isFrozen).toEqual(false);

    const stakeEntryOriginalMintTokenAccountId = await findAta(
      originalMintId2,
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
    expect(Number(checkUserRewardTokenAccount.amount)).toBeGreaterThan(1);
  });
});


