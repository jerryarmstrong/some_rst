src/programs/stakePool/utils.ts
===============================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import type { ParsedIdlAccountData } from "@cardinal/common";
import { withFindOrInitAssociatedTokenAccount } from "@cardinal/common";
import { AnchorProvider, BN, Program } from "@coral-xyz/anchor";
import type { Wallet } from "@coral-xyz/anchor/dist/cjs/provider";
import type {
  AccountMeta,
  Connection,
  PublicKey,
  Transaction,
} from "@solana/web3.js";

import type { CardinalStakePool } from "../../idl/cardinal_stake_pool";
import { getMintSupply } from "../../utils";
import type { REWARD_DISTRIBUTOR_PROGRAM } from "../rewardDistributor";
import {
  REWARD_DISTRIBUTOR_ADDRESS,
  REWARD_DISTRIBUTOR_IDL,
} from "../rewardDistributor";
import { findRewardDistributorId } from "../rewardDistributor/pda";
import type { STAKE_POOL_PROGRAM } from ".";
import { STAKE_POOL_ADDRESS, STAKE_POOL_IDL } from ".";
import { findStakeAuthorizationId, findStakeEntryId } from "./pda";

export const remainingAccountsForInitStakeEntry = (
  stakePoolId: PublicKey,
  originalMintId: PublicKey
): AccountMeta[] => {
  const stakeAuthorizationRecordId = findStakeAuthorizationId(
    stakePoolId,
    originalMintId
  );
  return [
    {
      pubkey: stakeAuthorizationRecordId,
      isSigner: false,
      isWritable: false,
    },
  ];
};

export const withRemainingAccountsForUnstake = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  stakeEntryId: PublicKey,
  receiptMint: PublicKey | null | undefined
): Promise<AccountMeta[]> => {
  if (receiptMint) {
    const stakeEntryReceiptMintTokenAccount =
      await withFindOrInitAssociatedTokenAccount(
        transaction,
        connection,
        receiptMint,
        stakeEntryId,
        wallet.publicKey,
        true
      );
    return [
      {
        pubkey: stakeEntryReceiptMintTokenAccount,
        isSigner: false,
        isWritable: false,
      },
    ];
  } else {
    return [];
  }
};

/**
 * Convenience method to find the stake entry id from a mint
 * NOTE: This will lookup the mint on-chain to get the supply
 * @returns
 */
export const findStakeEntryIdFromMint = async (
  connection: Connection,
  wallet: PublicKey,
  stakePoolId: PublicKey,
  originalMintId: PublicKey,
  isFungible?: boolean
): Promise<PublicKey> => {
  if (isFungible === undefined) {
    const supply = await getMintSupply(connection, originalMintId);
    isFungible = supply.gt(new BN(1));
  }
  return findStakeEntryId(wallet, stakePoolId, originalMintId, isFungible);
};

export const getTotalStakeSeconds = async (
  connection: Connection,
  stakeEntryId: PublicKey
): Promise<BN> => {
  // eslint-disable-next-line @typescript-eslint/ban-ts-comment
  // @ts-ignore
  const provider = new AnchorProvider(connection, null, {});
  const stakePoolProgram = new Program<STAKE_POOL_PROGRAM>(
    STAKE_POOL_IDL,
    STAKE_POOL_ADDRESS,
    provider
  );
  const parsed = await stakePoolProgram.account.stakeEntry.fetch(stakeEntryId);
  return parsed.totalStakeSeconds;
};

export const getActiveStakeSeconds = async (
  connection: Connection,
  stakeEntryId: PublicKey
): Promise<BN> => {
  // eslint-disable-next-line @typescript-eslint/ban-ts-comment
  // @ts-ignore
  const provider = new AnchorProvider(connection, null, {});
  const stakePoolProgram = new Program<STAKE_POOL_PROGRAM>(
    STAKE_POOL_IDL,
    STAKE_POOL_ADDRESS,
    provider
  );
  const parsed = await stakePoolProgram.account.stakeEntry.fetch(stakeEntryId);

  const UTCNow = Math.floor(Date.now() / 1000);
  const lastStakedAt = parsed.lastStakedAt.toNumber() || UTCNow;
  return parsed.lastStaker ? new BN(UTCNow - lastStakedAt) : new BN(0);
};

export const getUnclaimedRewards = async (
  connection: Connection,
  stakePoolId: PublicKey
): Promise<BN> => {
  // eslint-disable-next-line @typescript-eslint/ban-ts-comment
  // @ts-ignore
  const provider = new AnchorProvider(connection, null, {});
  const rewardDistributor = new Program<REWARD_DISTRIBUTOR_PROGRAM>(
    REWARD_DISTRIBUTOR_IDL,
    REWARD_DISTRIBUTOR_ADDRESS,
    provider
  );

  const rewardDistributorId = findRewardDistributorId(stakePoolId);
  const parsed = await rewardDistributor.account.rewardDistributor.fetch(
    rewardDistributorId
  );
  return parsed.maxSupply
    ? new BN(parsed.maxSupply?.toNumber() - parsed.rewardsIssued.toNumber())
    : new BN(0);
};

export const getClaimedRewards = async (
  connection: Connection,
  stakePoolId: PublicKey
): Promise<BN> => {
  // eslint-disable-next-line @typescript-eslint/ban-ts-comment
  // @ts-ignore
  const provider = new AnchorProvider(connection, null, {});
  const rewardDistributor = new Program<REWARD_DISTRIBUTOR_PROGRAM>(
    REWARD_DISTRIBUTOR_IDL,
    REWARD_DISTRIBUTOR_ADDRESS,
    provider
  );

  const rewardDistributorId = findRewardDistributorId(stakePoolId);
  const parsed = await rewardDistributor.account.rewardDistributor.fetch(
    rewardDistributorId
  );
  return parsed.rewardsIssued;
};

export const shouldReturnReceipt = (
  stakePoolData: ParsedIdlAccountData<"stakePool", CardinalStakePool>,
  stakeEntryData: ParsedIdlAccountData<"stakeEntry", CardinalStakePool>
): boolean =>
  // no cooldown
  !stakePoolData.cooldownSeconds ||
  stakePoolData.cooldownSeconds === 0 ||
  (!!stakeEntryData?.cooldownStartSeconds &&
    Date.now() / 1000 - stakeEntryData.cooldownStartSeconds.toNumber() >=
      stakePoolData.cooldownSeconds);


