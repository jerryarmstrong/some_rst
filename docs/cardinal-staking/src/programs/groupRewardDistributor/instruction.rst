src/programs/groupRewardDistributor/instruction.ts
==================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import type { BN } from "@coral-xyz/anchor";
import type { Wallet } from "@coral-xyz/anchor/dist/cjs/provider";
import { TOKEN_PROGRAM_ID } from "@solana/spl-token";
import type { AccountMeta, Connection, PublicKey } from "@solana/web3.js";
import { Keypair, SystemProgram, Transaction } from "@solana/web3.js";

import type {
  GroupRewardDistributorMetadataKind,
  GroupRewardDistributorPoolKind,
} from "./constants";
import {
  GROUP_REWARD_MANAGER,
  GroupRewardDistributorKind,
  groupRewardDistributorProgram,
} from "./constants";
import { findGroupRewardDistributorId } from "./pda";
import { withRemainingAccountsForRewardKind } from "./utils";

export const initGroupRewardDistributor = async (
  connection: Connection,
  wallet: Wallet,
  params: {
    rewardAmount: BN;
    rewardDurationSeconds: BN;
    rewardKind: GroupRewardDistributorKind;
    metadataKind: GroupRewardDistributorMetadataKind;
    poolKind: GroupRewardDistributorPoolKind;
    authorizedPools: PublicKey[];
    authorizedCreators?: PublicKey[];
    supply?: BN;
    baseAdder?: BN;
    baseAdderDecimals?: number;
    baseMultiplier?: BN;
    baseMultiplierDecimals?: number;
    multiplierDecimals?: number;
    maxSupply?: BN;
    minCooldownSeconds?: number;
    minStakeSeconds?: number;
    groupCountMultiplier?: BN;
    groupCountMultiplierDecimals?: number;
    minGroupSize?: number;
    maxRewardSecondsReceived?: BN;

    rewardMintId: PublicKey;
  }
): Promise<[Transaction, PublicKey]> => {
  const program = groupRewardDistributorProgram(connection, wallet);
  const signers: Keypair[] = [];
  const id = Keypair.generate();
  signers.push(id);

  const groupRewardDistributorId = findGroupRewardDistributorId(id.publicKey);

  const transaction = new Transaction();

  const remainingAccountsForKind = await withRemainingAccountsForRewardKind(
    transaction,
    connection,
    wallet,
    groupRewardDistributorId,
    params.rewardKind || GroupRewardDistributorKind.Mint,
    params.rewardMintId
  );

  const instruction = await program.methods
    .initGroupRewardDistributor({
      id: id.publicKey,
      rewardAmount: params.rewardAmount,
      rewardDurationSeconds: params.rewardDurationSeconds,
      rewardKind: params.rewardKind,
      metadataKind: params.metadataKind,
      poolKind: params.poolKind,
      authorizedPools: params.authorizedPools,
      authorizedCreators: params.authorizedCreators || null,
      supply: params.supply || null,
      baseAdder: params.baseAdder || null,
      baseAdderDecimals: params.baseAdderDecimals || null,
      baseMultiplier: params.baseMultiplier || null,
      baseMultiplierDecimals: params.baseMultiplierDecimals || null,
      multiplierDecimals: params.multiplierDecimals || null,
      maxSupply: params.maxSupply || null,
      minCooldownSeconds: params.minCooldownSeconds || null,
      minStakeSeconds: params.minStakeSeconds || null,
      groupCountMultiplier: params.groupCountMultiplier || null,
      groupCountMultiplierDecimals: params.groupCountMultiplierDecimals || null,
      minGroupSize: params.minGroupSize || null,
      maxRewardSecondsReceived: params.maxRewardSecondsReceived || null,
    })
    .accounts({
      groupRewardDistributor: groupRewardDistributorId,
      rewardMint: params.rewardMintId,
      authority: wallet.publicKey,
      payer: wallet.publicKey,
      tokenProgram: TOKEN_PROGRAM_ID,
      systemProgram: SystemProgram.programId,
    })
    .remainingAccounts(remainingAccountsForKind)
    .instruction();

  transaction.add(instruction);
  return [transaction, groupRewardDistributorId];
};

export const initGroupRewardCounter = async (
  connection: Connection,
  wallet: Wallet,
  params: {
    groupRewardCounterId: PublicKey;
    groupRewardDistributorId: PublicKey;
    authority?: PublicKey;
  }
): Promise<Transaction> => {
  const program = groupRewardDistributorProgram(connection, wallet);

  return program.methods
    .initGroupRewardCounter()
    .accounts({
      groupRewardCounter: params.groupRewardCounterId,
      groupRewardDistributor: params.groupRewardDistributorId,
      authority: params.authority,
      systemProgram: SystemProgram.programId,
    })
    .transaction();
};

export const initGroupRewardEntry = (
  connection: Connection,
  wallet: Wallet,
  params: {
    groupEntryId: PublicKey;
    groupRewardDistributorId: PublicKey;
    groupRewardEntryId: PublicKey;
    groupRewardCounterId: PublicKey;
    authority?: PublicKey;
    stakeEntries: {
      stakeEntryId: PublicKey;
      originalMint: PublicKey;
      originalMintMetadata: PublicKey;
      rewardEntryId: PublicKey;
    }[];
  }
): Promise<Transaction> => {
  const program = groupRewardDistributorProgram(connection, wallet);
  const remainingAccounts: AccountMeta[] = [];
  params.stakeEntries.forEach(
    ({ stakeEntryId, originalMint, originalMintMetadata, rewardEntryId }) => {
      remainingAccounts.push(
        {
          pubkey: stakeEntryId,
          isSigner: false,
          isWritable: false,
        },
        {
          pubkey: originalMint,
          isSigner: false,
          isWritable: false,
        },
        {
          pubkey: originalMintMetadata,
          isSigner: false,
          isWritable: false,
        },
        {
          pubkey: rewardEntryId,
          isSigner: false,
          isWritable: false,
        }
      );
    }
  );

  return program.methods
    .initGroupRewardEntry()
    .accounts({
      groupEntry: params.groupEntryId,
      groupRewardDistributor: params.groupRewardDistributorId,
      groupRewardEntry: params.groupRewardEntryId,
      groupRewardCounter: params.groupRewardCounterId,
      authority: params.authority ?? wallet.publicKey,
      systemProgram: SystemProgram.programId,
    })
    .remainingAccounts(remainingAccounts)
    .transaction();
};

export const claimGroupRewards = (
  connection: Connection,
  wallet: Wallet,
  params: {
    groupEntryId: PublicKey;
    groupRewardEntryId: PublicKey;
    groupRewardDistributorId: PublicKey;
    groupRewardCounterId: PublicKey;
    rewardMintId: PublicKey;
    userRewardMintTokenAccount: PublicKey;
    remainingAccountsForKind: AccountMeta[];
    authority?: PublicKey;
  }
): Promise<Transaction> => {
  const program = groupRewardDistributorProgram(connection, wallet);

  return program.methods
    .claimGroupRewards()
    .accounts({
      groupEntry: params.groupEntryId,
      groupRewardEntry: params.groupRewardEntryId,
      groupRewardDistributor: params.groupRewardDistributorId,
      groupRewardCounter: params.groupRewardCounterId,
      rewardMint: params.rewardMintId,
      userRewardMintTokenAccount: params.userRewardMintTokenAccount,
      rewardManager: GROUP_REWARD_MANAGER,
      authority: params.authority ?? wallet.publicKey,
      tokenProgram: TOKEN_PROGRAM_ID,
      systemProgram: SystemProgram.programId,
    })
    .remainingAccounts(params.remainingAccountsForKind)
    .transaction();
};

export const closeGroupRewardDistributor = async (
  connection: Connection,
  wallet: Wallet,
  params: {
    groupRewardDistributorId: PublicKey;
    rewardMintId: PublicKey;
    remainingAccountsForKind: AccountMeta[];
  }
): Promise<Transaction> => {
  const program = groupRewardDistributorProgram(connection, wallet);

  return program.methods
    .closeGroupRewardDistributor()
    .accounts({
      groupRewardDistributor: params.groupRewardDistributorId,
      rewardMint: params.rewardMintId,
      authority: wallet.publicKey,
      tokenProgram: TOKEN_PROGRAM_ID,
    })
    .remainingAccounts(params.remainingAccountsForKind)
    .transaction();
};

export const updateGroupRewardEntry = async (
  connection: Connection,
  wallet: Wallet,
  params: {
    groupRewardDistributorId: PublicKey;
    groupRewardEntryId: PublicKey;
    multiplier: BN;
  }
): Promise<Transaction> => {
  const program = groupRewardDistributorProgram(connection, wallet);

  return program.methods
    .updateGroupRewardEntry({
      multiplier: params.multiplier,
    })
    .accounts({
      groupRewardDistributor: params.groupRewardDistributorId,
      groupRewardEntry: params.groupRewardEntryId,
      authority: wallet.publicKey,
    })
    .transaction();
};

export const closeGroupRewardEntry = async (
  connection: Connection,
  wallet: Wallet,
  params: {
    groupEntryId: PublicKey;
    groupRewardEntryId: PublicKey;
    groupRewardDistributorId: PublicKey;
    groupRewardCounterId: PublicKey;
  }
): Promise<Transaction> => {
  const program = groupRewardDistributorProgram(connection, wallet);

  return program.methods
    .closeGroupRewardEntry()
    .accounts({
      groupEntry: params.groupEntryId,
      groupRewardEntry: params.groupRewardEntryId,
      authority: wallet.publicKey,
      groupRewardDistributor: params.groupRewardDistributorId,
      groupRewardCounter: params.groupRewardCounterId,
    })
    .transaction();
};

export const closeGroupRewardCounter = async (
  connection: Connection,
  wallet: Wallet,
  params: {
    groupRewardCounterId: PublicKey;
    groupRewardDistributorId: PublicKey;
    authority?: PublicKey;
  }
): Promise<Transaction> => {
  const program = groupRewardDistributorProgram(connection, wallet);

  return program.methods
    .closeGroupRewardCounter()
    .accounts({
      groupRewardCounter: params.groupRewardCounterId,
      groupRewardDistributor: params.groupRewardDistributorId,
      authority: params.authority,
    })
    .transaction();
};

export const updateGroupRewardDistributor = (
  connection: Connection,
  wallet: Wallet,
  params: {
    groupRewardDistributorId: PublicKey;
    rewardAmount: BN;
    rewardDurationSeconds: BN;
    metadataKind: GroupRewardDistributorMetadataKind;
    poolKind: GroupRewardDistributorPoolKind;
    authorizedPools: PublicKey[];
    authorizedCreators?: PublicKey[];
    baseAdder?: BN;
    baseAdderDecimals?: number;
    baseMultiplier?: BN;
    baseMultiplierDecimals?: number;
    multiplierDecimals?: number;
    maxSupply?: BN;
    minCooldownSeconds?: number;
    minStakeSeconds?: number;
    groupCountMultiplier?: BN;
    groupCountMultiplierDecimals?: number;
    minGroupSize?: number;
    maxRewardSecondsReceived?: BN;
  }
): Promise<Transaction> => {
  const program = groupRewardDistributorProgram(connection, wallet);

  return program.methods
    .updateGroupRewardDistributor({
      rewardAmount: params.rewardAmount,
      rewardDurationSeconds: params.rewardDurationSeconds,
      metadataKind: params.metadataKind,
      poolKind: params.poolKind,
      authorizedPools: params.authorizedPools,
      authorizedCreators: params.authorizedCreators || null,
      baseAdder: params.baseAdder || null,
      baseAdderDecimals: params.baseAdderDecimals || null,
      baseMultiplier: params.baseMultiplier || null,
      baseMultiplierDecimals: params.baseMultiplierDecimals || null,
      multiplierDecimals: params.multiplierDecimals || null,
      maxSupply: params.maxSupply || null,
      minCooldownSeconds: params.minCooldownSeconds || null,
      minStakeSeconds: params.minStakeSeconds || null,
      groupCountMultiplier: params.groupCountMultiplier || null,
      groupCountMultiplierDecimals: params.groupCountMultiplierDecimals || null,
      minGroupSize: params.minGroupSize || null,
      maxRewardSecondsReceived: params.maxRewardSecondsReceived || null,
    })
    .accounts({
      groupRewardDistributor: params.groupRewardDistributorId,
      authority: wallet.publicKey,
    })
    .transaction();
};

export const reclaimGroupFunds = (
  connection: Connection,
  wallet: Wallet,
  params: {
    groupRewardDistributorId: PublicKey;
    groupRewardDistributorTokenAccountId: PublicKey;
    authorityTokenAccountId: PublicKey;
    authority: PublicKey;
    amount: BN;
  }
): Promise<Transaction> => {
  const program = groupRewardDistributorProgram(connection, wallet);

  return program.methods
    .reclaimGroupFunds(params.amount)
    .accounts({
      groupRewardDistributor: params.groupRewardDistributorId,
      groupRewardDistributorTokenAccount:
        params.groupRewardDistributorTokenAccountId,
      authorityTokenAccount: params.authorityTokenAccountId,
      authority: wallet.publicKey,
      tokenProgram: TOKEN_PROGRAM_ID,
    })
    .transaction();
};


