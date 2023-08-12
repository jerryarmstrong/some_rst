src/utils.ts
============

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import type { AccountData } from "@cardinal/common";
import type { web3 } from "@coral-xyz/anchor";
import { BN } from "@coral-xyz/anchor";
import type { Wallet } from "@coral-xyz/anchor/dist/cjs/provider";
import {
  getAccount,
  getAssociatedTokenAddressSync,
  getMint,
} from "@solana/spl-token";
import type {
  ConfirmOptions,
  Connection,
  PublicKey,
  SendTransactionError,
  Signer,
  Transaction,
} from "@solana/web3.js";
import { sendAndConfirmRawTransaction } from "@solana/web3.js";

import type {
  GroupRewardCounterData,
  GroupRewardDistributorData,
  GroupRewardEntryData,
} from "./programs/groupRewardDistributor";
import type {
  RewardDistributorData,
  RewardEntryData,
} from "./programs/rewardDistributor";
import { getRewardEntries } from "./programs/rewardDistributor/accounts";
import { findRewardEntryId } from "./programs/rewardDistributor/pda";
import type { GroupStakeEntryData, StakeEntryData } from "./programs/stakePool";
import { getStakeEntries } from "./programs/stakePool/accounts";
import { findStakeEntryIdFromMint } from "./programs/stakePool/utils";

export const executeTransaction = async (
  connection: Connection,
  wallet: Wallet,
  transaction: Transaction,
  config: {
    silent?: boolean;
    signers?: Signer[];
    confirmOptions?: ConfirmOptions;
    callback?: (success: boolean) => void;
  }
): Promise<string> => {
  let txid = "";
  try {
    transaction.feePayer = wallet.publicKey;
    transaction.recentBlockhash = (
      await connection.getRecentBlockhash("max")
    ).blockhash;
    transaction = await wallet.signTransaction(transaction);
    if (config.signers && config.signers.length > 0) {
      transaction.partialSign(...config.signers);
    }
    txid = await sendAndConfirmRawTransaction(
      connection,
      transaction.serialize(),
      config.confirmOptions
    );
    config.callback && config.callback(true);
  } catch (e: unknown) {
    console.log("Failed transaction: ", (e as SendTransactionError).logs, e);
    config.callback && config.callback(false);
    if (!config.silent) {
      throw e;
    }
  }
  return txid;
};

/**
 * Get total supply of mint
 * @param connection
 * @param originalMintId
 * @returns
 */
export const getMintSupply = async (
  connection: web3.Connection,
  originalMintId: web3.PublicKey
): Promise<BN> => {
  return new BN((await getMint(connection, originalMintId)).supply.toString());
};

/**
 * Get pending rewards of mintIds for a given reward distributor
 * @param connection
 * @param wallet
 * @param mintIds
 * @param rewardDistributor
 * @returns
 */
export const getPendingRewardsForPool = async (
  connection: Connection,
  wallet: PublicKey,
  mintIds: PublicKey[],
  rewardDistributor: AccountData<RewardDistributorData>,
  UTCNow: number
): Promise<{
  rewardMap: {
    [mintId: string]: { claimableRewards: BN; nextRewardsIn: BN };
  };
  claimableRewards: BN;
}> => {
  const rewardDistributorTokenAccount = getAssociatedTokenAddressSync(
    rewardDistributor.parsed.rewardMint,
    rewardDistributor.pubkey,
    true
  );
  const rewardDistributorTokenAccountInfo = await getAccount(
    connection,
    rewardDistributorTokenAccount
  );

  const stakeEntryIds: PublicKey[] = await Promise.all(
    mintIds.map(async (mintId) =>
      findStakeEntryIdFromMint(
        connection,
        wallet,
        rewardDistributor.parsed.stakePool,
        mintId
      )
    )
  );

  const rewardEntryIds = stakeEntryIds.map((stakeEntryId) =>
    findRewardEntryId(rewardDistributor.pubkey, stakeEntryId)
  );

  const [stakeEntries, rewardEntries] = await Promise.all([
    getStakeEntries(connection, stakeEntryIds),
    getRewardEntries(connection, rewardEntryIds),
  ]);

  return getRewardMap(
    stakeEntries,
    rewardEntries,
    rewardDistributor,
    new BN(rewardDistributorTokenAccountInfo.amount.toString()),
    UTCNow
  );
};

/**
 * Get the map of rewards for stakeEntry to rewards and next reward time
 * Also return the total claimable rewards from this map
 * @param stakeEntries
 * @param rewardEntries
 * @param rewardDistributor
 * @param remainingRewardAmount
 * @returns
 */
export const getRewardMap = (
  stakeEntries: AccountData<StakeEntryData>[],
  rewardEntries: AccountData<RewardEntryData>[],
  rewardDistributor: AccountData<RewardDistributorData>,
  remainingRewardAmount: BN,
  UTCNow: number
): {
  rewardMap: {
    [stakeEntryId: string]: { claimableRewards: BN; nextRewardsIn: BN };
  };
  claimableRewards: BN;
} => {
  const rewardMap: {
    [stakeEntryId: string]: { claimableRewards: BN; nextRewardsIn: BN };
  } = {};

  for (let i = 0; i < stakeEntries.length; i++) {
    const stakeEntry = stakeEntries[i]!;
    const rewardEntry = rewardEntries.find((rewardEntry) =>
      rewardEntry?.parsed?.stakeEntry.equals(stakeEntry?.pubkey)
    );

    if (stakeEntry) {
      const [claimableRewards, nextRewardsIn] = calculatePendingRewards(
        rewardDistributor,
        stakeEntry,
        rewardEntry,
        remainingRewardAmount,
        UTCNow
      );
      rewardMap[stakeEntry.pubkey.toString()] = {
        claimableRewards,
        nextRewardsIn,
      };
    }
  }

  // Compute too many rewards
  let claimableRewards = Object.values(rewardMap).reduce(
    (acc, { claimableRewards }) => acc.add(claimableRewards),
    new BN(0)
  );
  if (
    rewardDistributor.parsed.maxSupply &&
    rewardDistributor.parsed.rewardsIssued
      .add(claimableRewards)
      .gte(rewardDistributor.parsed.maxSupply)
  ) {
    claimableRewards = rewardDistributor.parsed.maxSupply.sub(
      rewardDistributor.parsed.rewardsIssued
    );
  }

  if (claimableRewards.gt(remainingRewardAmount)) {
    claimableRewards = remainingRewardAmount;
  }
  return { rewardMap, claimableRewards };
};

/**
 * Calculate claimable rewards and next reward time for a give mint and reward and stake entry
 * @param rewardDistributor
 * @param stakeEntry
 * @param rewardEntry
 * @param remainingRewardAmount
 * @param UTCNow
 * @returns
 */
export const calculatePendingRewards = (
  rewardDistributor: AccountData<RewardDistributorData>,
  stakeEntry: AccountData<StakeEntryData>,
  rewardEntry: AccountData<RewardEntryData> | undefined,
  remainingRewardAmount: BN,
  UTCNow: number
): [BN, BN] => {
  if (
    !stakeEntry ||
    stakeEntry.parsed.pool.toString() !==
      rewardDistributor.parsed.stakePool.toString()
  ) {
    return [new BN(0), new BN(0)];
  }

  const rewardSecondsReceived =
    rewardEntry?.parsed.rewardSecondsReceived || new BN(0);
  const multiplier =
    rewardEntry?.parsed?.multiplier ||
    rewardDistributor.parsed.defaultMultiplier;

  let rewardSeconds = (stakeEntry.parsed.cooldownStartSeconds || new BN(UTCNow))
    .sub(stakeEntry.parsed.lastUpdatedAt ?? stakeEntry.parsed.lastStakedAt)
    .mul(stakeEntry.parsed.amount)
    .add(stakeEntry.parsed.totalStakeSeconds);
  if (rewardDistributor.parsed.maxRewardSecondsReceived) {
    rewardSeconds = BN.min(
      rewardSeconds,
      rewardDistributor.parsed.maxRewardSecondsReceived
    );
  }
  let rewardAmountToReceive = rewardSeconds
    .sub(rewardSecondsReceived)
    .div(rewardDistributor.parsed.rewardDurationSeconds)
    .mul(rewardDistributor.parsed.rewardAmount)
    .mul(multiplier)
    .div(new BN(10).pow(new BN(rewardDistributor.parsed.multiplierDecimals)));

  if (
    rewardDistributor.parsed.maxSupply &&
    rewardDistributor.parsed.rewardsIssued
      .add(rewardAmountToReceive)
      .gte(rewardDistributor.parsed.maxSupply)
  ) {
    rewardAmountToReceive = rewardDistributor.parsed.maxSupply.sub(
      rewardDistributor.parsed.rewardsIssued
    );
  }

  if (rewardAmountToReceive.gt(remainingRewardAmount)) {
    rewardAmountToReceive = remainingRewardAmount;
  }

  const nextRewardsIn = rewardDistributor.parsed.rewardDurationSeconds.sub(
    (stakeEntry.parsed.cooldownStartSeconds || new BN(UTCNow))
      .sub(stakeEntry.parsed.lastUpdatedAt ?? stakeEntry.parsed.lastStakedAt)
      .add(stakeEntry.parsed.totalStakeSeconds)
      .mod(rewardDistributor.parsed.rewardDurationSeconds)
  );

  return [rewardAmountToReceive, nextRewardsIn];
};

/**
 * Calculate claimable groupRewards and next groupReward time for a give mint and groupReward and stake entry
 * @param groupRewardDistributor
 * @param groupEntry
 * @param groupRewardEntry
 * @param remainingGroupRewardAmount
 * @param UTCNow
 * @returns
 */
export const calculatePendingGroupRewards = (
  groupRewardDistributor: AccountData<GroupRewardDistributorData>,
  groupEntry: AccountData<GroupStakeEntryData>,
  groupRewardEntry: AccountData<GroupRewardEntryData> | undefined,
  groupRewardCounter: AccountData<GroupRewardCounterData> | undefined,
  remainingGroupRewardAmount: BN,
  UTCNow: number
): [BN, BN] => {
  const rewardSecondsReceived =
    groupRewardEntry?.parsed.rewardSecondsReceived || new BN(0);
  const multiplier = groupRewardEntry?.parsed?.multiplier || new BN(1);

  let groupRewardSeconds = (
    groupEntry.parsed.groupCooldownStartSeconds || new BN(UTCNow)
  ).sub(groupEntry.parsed.changedAt);
  if (groupRewardDistributor.parsed.maxRewardSecondsReceived) {
    groupRewardSeconds = BN.min(
      groupRewardSeconds,
      groupRewardDistributor.parsed.maxRewardSecondsReceived
    );
  }
  let groupRewardAmountToReceive = groupRewardSeconds
    .sub(rewardSecondsReceived)
    .div(groupRewardDistributor.parsed.rewardDurationSeconds)
    .mul(groupRewardDistributor.parsed.rewardAmount)
    .mul(
      multiplier
        .mul(groupRewardDistributor.parsed.baseMultiplier)
        .div(
          new BN(10).pow(
            new BN(groupRewardDistributor.parsed.baseMultiplierDecimals)
          )
        )
        .add(
          groupRewardDistributor.parsed.baseAdder.div(
            new BN(10).pow(
              new BN(groupRewardDistributor.parsed.baseAdderDecimals)
            )
          )
        )
    )
    .div(
      new BN(10).pow(new BN(groupRewardDistributor.parsed.multiplierDecimals))
    );

  if (
    groupRewardDistributor.parsed.groupCountMultiplier &&
    groupRewardCounter
  ) {
    groupRewardAmountToReceive = groupRewardAmountToReceive
      .mul(groupRewardCounter.parsed.count)
      .div(groupRewardDistributor.parsed.groupCountMultiplier)
      .div(
        new BN(10).pow(
          new BN(
            groupRewardDistributor.parsed.groupCountMultiplierDecimals || 0
          )
        )
      );
  }

  if (
    groupRewardDistributor.parsed.maxSupply &&
    groupRewardDistributor.parsed.rewardsIssued
      .add(groupRewardAmountToReceive)
      .gte(groupRewardDistributor.parsed.maxSupply)
  ) {
    groupRewardAmountToReceive = groupRewardDistributor.parsed.maxSupply.sub(
      groupRewardDistributor.parsed.rewardsIssued
    );
  }

  if (groupRewardAmountToReceive.gt(remainingGroupRewardAmount)) {
    groupRewardAmountToReceive = remainingGroupRewardAmount;
  }

  const nextRewardsIn = groupRewardDistributor.parsed.rewardDurationSeconds.sub(
    (groupEntry.parsed.groupCooldownStartSeconds || new BN(UTCNow))
      .sub(groupEntry.parsed.changedAt)
      .mod(groupRewardDistributor.parsed.rewardDurationSeconds)
  );

  return [groupRewardAmountToReceive, nextRewardsIn];
};


