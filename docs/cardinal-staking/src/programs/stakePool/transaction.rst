src/programs/stakePool/transaction.ts
=====================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import {
  findMintMetadataId,
  METADATA_PROGRAM_ID,
  tryGetAccount,
  withFindOrInitAssociatedTokenAccount,
} from "@cardinal/common";
import { PAYMENT_MANAGER_ADDRESS } from "@cardinal/payment-manager";
import { getPaymentManager } from "@cardinal/payment-manager/dist/cjs/accounts";
import { TOKEN_MANAGER_ADDRESS } from "@cardinal/token-manager/dist/cjs/programs/tokenManager";
import { findMintManagerId } from "@cardinal/token-manager/dist/cjs/programs/tokenManager/pda";
import { BN } from "@coral-xyz/anchor";
import type { Wallet } from "@coral-xyz/anchor/dist/cjs/provider";
import { ASSOCIATED_PROGRAM_ID } from "@coral-xyz/anchor/dist/cjs/utils/token";
import {
  getAssociatedTokenAddressSync,
  TOKEN_PROGRAM_ID,
} from "@solana/spl-token";
import type { Connection, PublicKey, Transaction } from "@solana/web3.js";
import {
  Keypair,
  SystemProgram,
  SYSVAR_RENT_PUBKEY,
  SYSVAR_SLOT_HASHES_PUBKEY,
} from "@solana/web3.js";

import { getPoolIdentifier, getStakeBooster, getStakeEntry } from "./accounts";
import { STAKE_BOOSTER_PAYMENT_MANAGER, stakePoolProgram } from "./constants";
import {
  findGroupEntryId,
  findIdentifierId,
  findStakeAuthorizationId,
  findStakeBoosterId,
  findStakePoolId,
} from "./pda";
import { remainingAccountsForInitStakeEntry } from "./utils";

export const withInitStakePool = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  params: {
    requiresCollections?: PublicKey[];
    requiresCreators?: PublicKey[];
    requiresAuthorization?: boolean;
    overlayText?: string;
    imageUri?: string;
    resetOnStake?: boolean;
    cooldownSeconds?: number;
    minStakeSeconds?: number;
    endDate?: BN;
    doubleOrResetEnabled?: boolean;
  }
): Promise<[Transaction, PublicKey]> => {
  const identifierId = findIdentifierId();
  const identifierData = await tryGetAccount(() =>
    getPoolIdentifier(connection)
  );
  const identifier = identifierData?.parsed.count || new BN(1);

  const program = stakePoolProgram(connection, wallet);
  if (!identifierData) {
    const ix = await program.methods
      .initIdentifier()
      .accounts({
        identifier: identifierId,
        payer: wallet.publicKey,
        systemProgram: SystemProgram.programId,
      })
      .instruction();
    transaction.add(ix);
  }

  const stakePoolId = findStakePoolId(identifier);
  const ix = await program.methods
    .initPool({
      overlayText: params.overlayText || "STAKED",
      imageUri: params.imageUri || "",
      requiresCollections: params.requiresCollections || [],
      requiresCreators: params.requiresCreators || [],
      requiresAuthorization: params.requiresAuthorization || false,
      authority: wallet.publicKey,
      resetOnStake: params.resetOnStake || false,
      cooldownSeconds: params.cooldownSeconds || null,
      minStakeSeconds: params.minStakeSeconds || null,
      endDate: params.endDate || null,
      doubleOrResetEnabled: params.doubleOrResetEnabled || null,
    })
    .accounts({
      stakePool: stakePoolId,
      identifier: identifierId,
      payer: wallet.publicKey,
      systemProgram: SystemProgram.programId,
    })
    .instruction();
  transaction.add(ix);
  return [transaction, stakePoolId];
};

/**
 * Add init stake entry instructions to a transaction
 * @param transaction
 * @param connection
 * @param wallet
 * @param params
 * @returns Transaction, public key for the created stake entry
 */
export const withInitStakeEntry = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  params: {
    stakePoolId: PublicKey;
    stakeEntryId: PublicKey;
    originalMintId: PublicKey;
  }
): Promise<Transaction> => {
  const ix = await stakePoolProgram(connection, wallet)
    .methods.initEntry(wallet.publicKey)
    .accountsStrict({
      stakeEntry: params.stakeEntryId,
      stakePool: params.stakePoolId,
      originalMint: params.originalMintId,
      originalMintMetadata: findMintMetadataId(params.originalMintId),
      payer: wallet.publicKey,
      systemProgram: SystemProgram.programId,
    })
    .remainingAccounts(
      remainingAccountsForInitStakeEntry(
        params.stakePoolId,
        params.originalMintId
      )
    )
    .instruction();
  transaction.add(ix);
  return transaction;
};

/**
 * Add authorize stake entry instructions to a transaction
 * @param transaction
 * @param connection
 * @param wallet
 * @param params
 * @returns Transaction
 */
export const withAuthorizeStakeEntry = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  params: {
    stakePoolId: PublicKey;
    originalMintId: PublicKey;
  }
): Promise<Transaction> => {
  const ix = await stakePoolProgram(connection, wallet)
    .methods.authorizeMint(params.originalMintId)
    .accounts({
      stakePool: params.stakePoolId,
      stakeAuthorizationRecord: findStakeAuthorizationId(
        params.stakePoolId,
        params.originalMintId
      ),
      payer: wallet.publicKey,
      systemProgram: SystemProgram.programId,
    })
    .instruction();
  transaction.add(ix);
  return transaction;
};

/**
 * Add authorize stake entry instructions to a transaction
 * @param transaction
 * @param connection
 * @param wallet
 * @param params
 * @returns Transaction
 */
export const withDeauthorizeStakeEntry = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  params: {
    stakePoolId: PublicKey;
    originalMintId: PublicKey;
  }
): Promise<Transaction> => {
  const stakeAuthorizationId = findStakeAuthorizationId(
    params.stakePoolId,
    params.originalMintId
  );

  const program = stakePoolProgram(connection, wallet);
  const ix = await program.methods
    .deauthorizeMint()
    .accounts({
      stakePool: params.stakePoolId,
      stakeAuthorizationRecord: stakeAuthorizationId,
      authority: wallet.publicKey,
    })
    .instruction();
  transaction.add(ix);
  return transaction;
};

/**
 * Add init stake mint instructions to a transaction
 * @param transaction
 * @param connection
 * @param wallet
 * @param params
 * @returns Transaction, keypair of the created stake mint
 */
export const withInitStakeMint = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  params: {
    stakePoolId: PublicKey;
    stakeEntryId: PublicKey;
    originalMintId: PublicKey;
    stakeMintKeypair: Keypair;
    name: string;
    symbol: string;
  }
): Promise<[Transaction, Keypair]> => {
  const originalMintMetadataId = findMintMetadataId(params.originalMintId);
  const stakeMintMetadataId = findMintMetadataId(
    params.stakeMintKeypair.publicKey
  );
  const stakeEntryStakeMintTokenAccountId = getAssociatedTokenAddressSync(
    params.stakeMintKeypair.publicKey,
    params.stakeEntryId,
    true
  );

  const program = stakePoolProgram(connection, wallet);
  const ix = await program.methods
    .initStakeMint({
      name: params.name,
      symbol: params.symbol,
    })
    .accounts({
      stakeEntry: params.stakeEntryId,
      stakePool: params.stakePoolId,
      originalMint: params.originalMintId,
      originalMintMetadata: originalMintMetadataId,
      stakeMint: params.stakeMintKeypair.publicKey,
      stakeMintMetadata: stakeMintMetadataId,
      stakeEntryStakeMintTokenAccount: stakeEntryStakeMintTokenAccountId,
      mintManager: findMintManagerId(params.stakeMintKeypair.publicKey),
      payer: wallet.publicKey,
      rent: SYSVAR_RENT_PUBKEY,
      tokenProgram: TOKEN_PROGRAM_ID,
      tokenManagerProgram: TOKEN_MANAGER_ADDRESS,
      associatedToken: ASSOCIATED_PROGRAM_ID,
      tokenMetadataProgram: METADATA_PROGRAM_ID,
      systemProgram: SystemProgram.programId,
    })
    .instruction();
  transaction.add(ix);
  return [transaction, params.stakeMintKeypair];
};

export const withUpdateStakePool = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  params: {
    stakePoolId: PublicKey;
    requiresCollections?: PublicKey[];
    requiresCreators?: PublicKey[];
    requiresAuthorization?: boolean;
    overlayText?: string;
    imageUri?: string;
    resetOnStake?: boolean;
    cooldownSeconds?: number;
    minStakeSeconds?: number;
    endDate?: BN;
    doubleOrResetEnabled?: boolean;
  }
): Promise<[Transaction, PublicKey]> => {
  const program = stakePoolProgram(connection, wallet);
  const ix = await program.methods
    .updatePool({
      imageUri: params.imageUri || "",
      overlayText: params.overlayText || "STAKED",
      requiresCollections: params.requiresCollections || [],
      requiresCreators: params.requiresCreators || [],
      requiresAuthorization: params.requiresAuthorization || false,
      authority: wallet.publicKey,
      resetOnStake: params.resetOnStake || false,
      cooldownSeconds: params.cooldownSeconds || null,
      minStakeSeconds: params.minStakeSeconds || null,
      endDate: params.endDate || null,
      doubleOrResetEnabled: params.doubleOrResetEnabled || null,
    })
    .accounts({
      stakePool: params.stakePoolId,
      payer: wallet.publicKey,
    })
    .instruction();
  transaction.add(ix);
  return [transaction, params.stakePoolId];
};

export const withUpdateTotalStakeSeconds = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  params: {
    stakeEntryId: PublicKey;
    lastStaker: PublicKey;
  }
): Promise<Transaction> => {
  const ix = await stakePoolProgram(connection, wallet)
    .methods.updateTotalStakeSeconds()
    .accounts({
      stakeEntry: params.stakeEntryId,
      lastStaker: params.lastStaker,
    })
    .instruction();
  transaction.add(ix);
  return transaction;
};

export const withCloseStakePool = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  params: {
    stakePoolId: PublicKey;
  }
): Promise<Transaction> => {
  const program = stakePoolProgram(connection, wallet);
  const ix = await program.methods
    .closeStakePool()
    .accounts({
      stakePool: params.stakePoolId,
      authority: wallet.publicKey,
    })
    .instruction();
  transaction.add(ix);
  return transaction;
};

export const withCloseStakeEntry = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  params: {
    stakePoolId: PublicKey;
    stakeEntryId: PublicKey;
  }
): Promise<Transaction> => {
  const program = stakePoolProgram(connection, wallet);
  const ix = await program.methods
    .closeStakeEntry()
    .accounts({
      stakePool: params.stakePoolId,
      stakeEntry: params.stakeEntryId,
      authority: wallet.publicKey,
    })
    .instruction();
  transaction.add(ix);
  return transaction;
};

export const withReassignStakeEntry = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  params: {
    stakePoolId: PublicKey;
    stakeEntryId: PublicKey;
    target: PublicKey;
  }
): Promise<Transaction> => {
  const program = stakePoolProgram(connection, wallet);
  const ix = await program.methods
    .reassignStakeEntry({ target: params.target })
    .accounts({
      stakePool: params.stakePoolId,
      stakeEntry: params.stakeEntryId,
      lastStaker: wallet.publicKey,
    })
    .instruction();
  transaction.add(ix);
  return transaction;
};

export const withDoubleOrResetTotalStakeSeconds = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  params: {
    stakePoolId: PublicKey;
    stakeEntryId: PublicKey;
  }
): Promise<Transaction> => {
  const program = stakePoolProgram(connection, wallet);
  const ix = await program.methods
    .doubleOrResetTotalStakeSeconds()
    .accounts({
      stakeEntry: params.stakeEntryId,
      stakePool: params.stakePoolId,
      lastStaker: wallet.publicKey,
      recentSlothashes: SYSVAR_SLOT_HASHES_PUBKEY,
    })
    .instruction();
  transaction.add(ix);
  return transaction;
};

export const withInitStakeBooster = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  params: {
    stakePoolId: PublicKey;
    stakeBoosterIdentifier?: BN;
    paymentAmount: BN;
    paymentMint: PublicKey;
    boostSeconds: BN;
    startTimeSeconds: number;
    payer?: PublicKey;
  }
): Promise<Transaction> => {
  const stakeBoosterId = findStakeBoosterId(
    params.stakePoolId,
    params.stakeBoosterIdentifier
  );
  const program = stakePoolProgram(connection, wallet);
  const ix = await program.methods
    .initStakeBooster({
      stakePool: params.stakePoolId,
      identifier: params.stakeBoosterIdentifier || new BN(0),
      paymentAmount: params.paymentAmount,
      paymentMint: params.paymentMint,
      paymentManager: STAKE_BOOSTER_PAYMENT_MANAGER,
      boostSeconds: params.boostSeconds,
      startTimeSeconds: new BN(params.startTimeSeconds),
    })
    .accounts({
      stakeBooster: stakeBoosterId,
      stakePool: params.stakePoolId,
      authority: wallet.publicKey,
      payer: wallet.publicKey,
      systemProgram: SystemProgram.programId,
    })
    .instruction();
  transaction.add(ix);
  return transaction;
};

export const withUpdateStakeBooster = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  params: {
    stakePoolId: PublicKey;
    stakeBoosterIdentifier?: BN;
    paymentAmount: BN;
    paymentMint: PublicKey;
    boostSeconds: BN;
    startTimeSeconds: number;
  }
): Promise<Transaction> => {
  const stakeBoosterId = findStakeBoosterId(
    params.stakePoolId,
    params.stakeBoosterIdentifier
  );
  const program = stakePoolProgram(connection, wallet);
  const ix = await program.methods
    .updateStakeBooster({
      paymentAmount: params.paymentAmount,
      paymentMint: params.paymentMint,
      paymentManager: STAKE_BOOSTER_PAYMENT_MANAGER,
      boostSeconds: params.boostSeconds,
      startTimeSeconds: new BN(params.startTimeSeconds),
    })
    .accounts({
      stakeBooster: stakeBoosterId,
      stakePool: params.stakePoolId,
      authority: wallet.publicKey,
    })
    .instruction();
  transaction.add(ix);
  return transaction;
};

export const withCloseStakeBooster = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  params: {
    stakePoolId: PublicKey;
    stakeBoosterIdentifier?: BN;
  }
): Promise<Transaction> => {
  const stakeBoosterId = findStakeBoosterId(
    params.stakePoolId,
    params.stakeBoosterIdentifier
  );
  const program = stakePoolProgram(connection, wallet);
  const ix = await program.methods
    .closeStakeBooster()
    .accounts({
      stakeBooster: stakeBoosterId,
      stakePool: params.stakePoolId,
      authority: wallet.publicKey,
    })
    .instruction();
  transaction.add(ix);
  return transaction;
};

export const withBoostStakeEntry = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  params: {
    stakePoolId: PublicKey;
    stakeBoosterIdentifier?: BN;
    stakeEntryId: PublicKey;
    originalMintId: PublicKey;
    payerTokenAccount: PublicKey;
    payer?: PublicKey;
    secondsToBoost: BN;
  }
): Promise<Transaction> => {
  const stakeBoosterId = findStakeBoosterId(
    params.stakePoolId,
    params.stakeBoosterIdentifier
  );

  const stakeBooster = await getStakeBooster(connection, stakeBoosterId);
  const paymentManager = await getPaymentManager(
    connection,
    stakeBooster.parsed.paymentManager
  );
  const feeCollectorTokenAccount = await withFindOrInitAssociatedTokenAccount(
    transaction,
    connection,
    stakeBooster.parsed.paymentMint,
    paymentManager.parsed.feeCollector,
    params.payer ?? wallet.publicKey
  );
  const paymentRecipientTokenAccount =
    await withFindOrInitAssociatedTokenAccount(
      transaction,
      connection,
      stakeBooster.parsed.paymentMint,
      stakeBooster.parsed.paymentRecipient,
      params.payer ?? wallet.publicKey
    );
  const program = stakePoolProgram(connection, wallet);
  const ix = await program.methods
    .boostStakeEntry({ secondsToBoost: params.secondsToBoost })
    .accounts({
      stakeBooster: stakeBooster.pubkey,
      stakePool: params.stakePoolId,
      stakeEntry: params.stakeEntryId,
      originalMint: params.originalMintId,
      payerTokenAccount: params.payerTokenAccount,
      paymentRecipientTokenAccount: paymentRecipientTokenAccount,
      payer: wallet.publicKey,
      paymentManager: stakeBooster.parsed.paymentManager,
      feeCollectorTokenAccount: feeCollectorTokenAccount,
      cardinalPaymentManager: PAYMENT_MANAGER_ADDRESS,
      tokenProgram: TOKEN_PROGRAM_ID,
      systemProgram: SystemProgram.programId,
    })
    .instruction();
  transaction.add(ix);
  return transaction;
};

/**
 * Add init group stake entry instructions to a transaction
 * @param transaction
 * @param connection
 * @param wallet
 * @param params
 * @returns Transaction, public key for the created group stake entry
 */
export const withInitGroupStakeEntry = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  params: {
    groupCooldownSeconds?: number;
    groupStakeSeconds?: number;
  }
): Promise<[Transaction, PublicKey]> => {
  const id = Keypair.generate();
  const program = stakePoolProgram(connection, wallet);
  const groupEntryId = findGroupEntryId(id.publicKey);
  const ix = await program.methods
    .initGroupEntry({
      groupId: id.publicKey,
      groupCooldownSeconds: params.groupCooldownSeconds || null,
      groupStakeSeconds: params.groupStakeSeconds || null,
    })
    .accounts({
      groupEntry: groupEntryId,
      authority: wallet.publicKey,
      systemProgram: SystemProgram.programId,
    })
    .instruction();
  transaction.add(ix);
  return [transaction, groupEntryId];
};

/**
 * Add a stake entry to the group entry instructions to a transaction
 * @param transaction
 * @param connection
 * @param wallet
 * @param params
 * @returns Transaction, public key for the created group stake entry
 */
export const withAddToGroupEntry = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  params: {
    groupEntryId: PublicKey;
    stakeEntryId: PublicKey;
    payer?: PublicKey;
  }
): Promise<[Transaction]> => {
  const program = stakePoolProgram(connection, wallet);
  const ix = await program.methods
    .addToGroupEntry()
    .accounts({
      groupEntry: params.groupEntryId,
      stakeEntry: params.stakeEntryId,
      authority: wallet.publicKey,
      payer: params.payer ?? wallet.publicKey,
      systemProgram: SystemProgram.programId,
    })
    .instruction();
  transaction.add(ix);
  return [transaction];
};

/**
 * Remove stake entry from the group entry instructions to a transaction
 * @param transaction
 * @param connection
 * @param wallet
 * @param params
 * @returns Transaction, public key for the created group stake entry
 */
export const withRemoveFromGroupEntry = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  params: {
    groupEntryId: PublicKey;
    stakeEntryId: PublicKey;
  }
): Promise<[Transaction]> => {
  const program = stakePoolProgram(connection, wallet);
  const ix = await program.methods
    .removeFromGroupEntry()
    .accounts({
      groupEntry: params.groupEntryId,
      stakeEntry: params.stakeEntryId,
      authority: wallet.publicKey,
      payer: wallet.publicKey,
      systemProgram: SystemProgram.programId,
    })
    .instruction();
  transaction.add(ix);
  return [transaction];
};

/**
 * Add init ungrouping instructions to a transaction
 * @param transaction
 * @param connection
 * @param wallet
 * @param params
 * @returns Transaction, public key for the created group stake entry
 */
export const withInitUngrouping = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  params: {
    groupEntryId: PublicKey;
  }
): Promise<[Transaction]> => {
  const program = stakePoolProgram(connection, wallet);
  const ix = await program.methods
    .initUngrouping()
    .accounts({
      groupEntry: params.groupEntryId,
      authority: wallet.publicKey,
    })
    .instruction();
  transaction.add(ix);
  return [transaction];
};

export const withClaimStakeEntryFunds = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  stakeEntryId: PublicKey,
  fundsMintId: PublicKey
): Promise<[Transaction]> => {
  const program = stakePoolProgram(connection, wallet);
  const stakeEntryData = await tryGetAccount(() =>
    getStakeEntry(connection, stakeEntryId)
  );
  if (!stakeEntryData) {
    throw `No stake entry id with address ${stakeEntryId.toString()}`;
  }

  const stakeEntryFundsMintTokenAccountId = getAssociatedTokenAddressSync(
    fundsMintId,
    stakeEntryId,
    true
  );

  const userFundsMintTokenAccountId =
    await withFindOrInitAssociatedTokenAccount(
      transaction,
      connection,
      fundsMintId,
      stakeEntryData.parsed.lastStaker,
      wallet.publicKey,
      true
    );

  const ix = await program.methods
    .claimStakeEntryFunds()
    .accounts({
      fundsMint: fundsMintId,
      stakeEntryFundsMintTokenAccount: stakeEntryFundsMintTokenAccountId,
      userFundsMintTokenAccount: userFundsMintTokenAccountId,
      stakePool: stakeEntryData.parsed.pool,
      stakeEntry: stakeEntryId,
      originalMint: stakeEntryData.parsed.originalMint,
      authority: wallet.publicKey,
      tokenProgram: TOKEN_PROGRAM_ID,
    })
    .instruction();
  transaction.add(ix);
  return [transaction];
};


