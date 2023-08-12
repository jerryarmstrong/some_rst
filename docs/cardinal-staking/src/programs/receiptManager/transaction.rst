src/programs/receiptManager/transaction.ts
==========================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import {
  tryGetAccount,
  withFindOrInitAssociatedTokenAccount,
} from "@cardinal/common";
import { PAYMENT_MANAGER_ADDRESS } from "@cardinal/payment-manager";
import { getPaymentManager } from "@cardinal/payment-manager/dist/cjs/accounts";
import type { BN } from "@coral-xyz/anchor";
import type { Wallet } from "@coral-xyz/anchor/dist/cjs/provider";
import { TOKEN_PROGRAM_ID } from "@solana/spl-token";
import type { Connection, PublicKey, Transaction } from "@solana/web3.js";
import { SystemProgram } from "@solana/web3.js";

import { withUpdateTotalStakeSeconds } from "../stakePool/transaction";
import { getReceiptManager } from "./accounts";
import {
  RECEIPT_MANAGER_PAYMENT_MANAGER,
  receiptManagerProgram,
} from "./constants";
import {
  findReceiptEntryId,
  findReceiptManagerId,
  findRewardReceiptId,
} from "./pda";

export const withInitReceiptManager = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  params: {
    name: string;
    stakePoolId: PublicKey;
    authority: PublicKey;
    requiredStakeSeconds: BN;
    stakeSecondsToUse: BN;
    paymentMint: PublicKey;
    paymentManagerId?: PublicKey;
    paymentRecipientId: PublicKey;
    requiresAuthorization: boolean;
    maxClaimedReceipts?: BN;
  }
): Promise<[Transaction, PublicKey]> => {
  const receiptManagerId = findReceiptManagerId(
    params.stakePoolId,
    params.name
  );
  const program = receiptManagerProgram(connection, wallet);
  const ix = await program.methods
    .initReceiptManager({
      name: params.name,
      authority: params.authority,
      requiredStakeSeconds: params.requiredStakeSeconds,
      stakeSecondsToUse: params.stakeSecondsToUse,
      paymentMint: params.paymentMint,
      paymentManager:
        params.paymentManagerId || RECEIPT_MANAGER_PAYMENT_MANAGER,
      paymentRecipient: params.paymentRecipientId,
      requiresAuthorization: params.requiresAuthorization,
      maxClaimedReceipts: params.maxClaimedReceipts ?? null,
    })
    .accounts({
      receiptManager: receiptManagerId,
      stakePool: params.stakePoolId,
      payer: wallet.publicKey,
      systemProgram: SystemProgram.programId,
    })
    .instruction();
  transaction.add(ix);
  return [transaction, receiptManagerId];
};

export const withInitReceiptEntry = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  params: {
    stakeEntryId: PublicKey;
  }
): Promise<[Transaction, PublicKey]> => {
  const receiptEntryId = findReceiptEntryId(params.stakeEntryId);
  const program = receiptManagerProgram(connection, wallet);
  const ix = await program.methods
    .initReceiptEntry()
    .accounts({
      receiptEntry: receiptEntryId,
      stakeEntry: params.stakeEntryId,
      payer: wallet.publicKey,
      systemProgram: SystemProgram.programId,
    })
    .instruction();
  transaction.add(ix);
  return [transaction, receiptEntryId];
};

export const withInitRewardReceipt = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  params: {
    receiptManagerId: PublicKey;
    receiptEntryId: PublicKey;
    stakeEntryId: PublicKey;
    payer?: PublicKey;
  }
): Promise<[Transaction, PublicKey]> => {
  const rewardReceiptId = findRewardReceiptId(
    params.receiptManagerId,
    params.receiptEntryId
  );
  const program = receiptManagerProgram(connection, wallet);
  const ix = await program.methods
    .initRewardReceipt()
    .accounts({
      rewardReceipt: rewardReceiptId,
      receiptManager: params.receiptManagerId,
      receiptEntry: params.receiptEntryId,
      stakeEntry: params.stakeEntryId,
      payer: wallet.publicKey,
      systemProgram: SystemProgram.programId,
    })
    .instruction();
  transaction.add(ix);
  return [transaction, rewardReceiptId];
};

export const withUpdateReceiptManager = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  params: {
    name: string;
    stakePoolId: PublicKey;
    authority: PublicKey;
    requiredStakeSeconds: BN;
    stakeSecondsToUse: BN;
    paymentMint: PublicKey;
    paymentManagerId?: PublicKey;
    paymentRecipientId: PublicKey;
    requiresAuthorization: boolean;
    maxClaimedReceipts?: BN;
  }
): Promise<[Transaction, PublicKey]> => {
  const receiptManagerId = findReceiptManagerId(
    params.stakePoolId,
    params.name
  );
  const receiptManagerData = await getReceiptManager(
    connection,
    receiptManagerId
  );

  const program = receiptManagerProgram(connection, wallet);
  const ix = await program.methods
    .updateReceiptManager({
      authority: params.authority || receiptManagerData.parsed.authority,
      requiredStakeSeconds:
        params.requiredStakeSeconds ||
        receiptManagerData.parsed.requiredStakeSeconds,
      stakeSecondsToUse:
        params.stakeSecondsToUse || receiptManagerData.parsed.stakeSecondsToUse,
      paymentMint: params.paymentMint || receiptManagerData.parsed.paymentMint,
      paymentManager:
        params.paymentManagerId || receiptManagerData.parsed.paymentManager,
      paymentRecipient:
        params.paymentRecipientId || receiptManagerData.parsed.paymentRecipient,
      requiresAuthorization:
        params.requiresAuthorization ||
        receiptManagerData.parsed.requiresAuthorization,
      maxClaimedReceipts:
        params.maxClaimedReceipts ||
        receiptManagerData.parsed.maxClaimedReceipts,
    })
    .accounts({
      receiptManager: receiptManagerId,
      authority: wallet.publicKey,
    })
    .instruction();
  transaction.add(ix);
  return [transaction, receiptManagerId];
};

export const withClaimRewardReceipt = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  params: {
    receiptManagerName: string;
    stakePoolId: PublicKey;
    stakeEntryId: PublicKey;
    claimer: PublicKey;
    payer: PublicKey;
  }
): Promise<[Transaction, PublicKey]> => {
  const receiptManagerId = findReceiptManagerId(
    params.stakePoolId,
    params.receiptManagerName
  );
  const checkReceiptManager = await tryGetAccount(() =>
    getReceiptManager(connection, receiptManagerId)
  );
  if (!checkReceiptManager) {
    throw `No reward receipt manager found with name ${
      params.receiptManagerName
    } for pool ${params.stakePoolId.toString()}`;
  }
  const receiptEntryId = findReceiptEntryId(params.stakeEntryId);
  const rewardReceiptId = findRewardReceiptId(receiptManagerId, receiptEntryId);

  const checkPaymentManager = await tryGetAccount(() =>
    getPaymentManager(connection, checkReceiptManager.parsed.paymentManager)
  );
  if (!checkPaymentManager) {
    throw `Could not find payment manager with address ${checkReceiptManager.parsed.paymentManager.toString()}`;
  }

  const feeCollectorTokenAccountId = await withFindOrInitAssociatedTokenAccount(
    transaction,
    connection,
    checkReceiptManager.parsed.paymentMint,
    checkPaymentManager.parsed.feeCollector,
    wallet.publicKey
  );
  const paymentRecipientTokenAccountId =
    await withFindOrInitAssociatedTokenAccount(
      transaction,
      connection,
      checkReceiptManager.parsed.paymentMint,
      checkReceiptManager.parsed.paymentRecipient,
      params.payer ?? wallet.publicKey
    );
  const payerTokenAccountId = await withFindOrInitAssociatedTokenAccount(
    transaction,
    connection,
    checkReceiptManager.parsed.paymentMint,
    params.payer,
    wallet.publicKey
  );

  await withUpdateTotalStakeSeconds(transaction, connection, wallet, {
    stakeEntryId: params.stakeEntryId,
    lastStaker: params.claimer,
  });

  const program = receiptManagerProgram(connection, wallet);
  const ix = await program.methods
    .claimRewardReceipt()
    .accounts({
      rewardReceipt: rewardReceiptId,
      receiptManager: receiptManagerId,
      stakeEntry: params.stakeEntryId,
      receiptEntry: receiptEntryId,
      paymentManager: checkReceiptManager.parsed.paymentManager,
      feeCollectorTokenAccount: feeCollectorTokenAccountId,
      paymentRecipientTokenAccount: paymentRecipientTokenAccountId,
      payerTokenAccount: payerTokenAccountId,
      payer: wallet.publicKey,
      claimer: params.claimer,
      cardinalPaymentManager: PAYMENT_MANAGER_ADDRESS,
      tokenProgram: TOKEN_PROGRAM_ID,
      systemProgram: SystemProgram.programId,
    })
    .instruction();
  transaction.add(ix);
  return [transaction, rewardReceiptId];
};

export const withCloseReceiptManager = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  params: {
    receiptManagerId: PublicKey;
  }
): Promise<Transaction> => {
  const program = receiptManagerProgram(connection, wallet);
  const ix = await program.methods
    .closeReceiptManager()
    .accounts({
      receiptManager: params.receiptManagerId,
      authority: wallet.publicKey,
    })
    .instruction();
  transaction.add(ix);
  return transaction;
};

export const withCloseReceiptEntry = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  params: {
    receiptManagerId: PublicKey;
    receiptEntryId: PublicKey;
    stakeEntryId: PublicKey;
  }
): Promise<Transaction> => {
  const program = receiptManagerProgram(connection, wallet);
  const ix = await program.methods
    .closeReceiptEntry()
    .accounts({
      receiptEntry: params.receiptEntryId,
      receiptManager: params.receiptManagerId,
      stakeEntry: params.stakeEntryId,
      authority: wallet.publicKey,
    })
    .instruction();
  transaction.add(ix);
  return transaction;
};

export const withCloseRewardReceipt = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  params: {
    receiptManagerId: PublicKey;
    rewardReceiptId: PublicKey;
  }
): Promise<Transaction> => {
  const program = receiptManagerProgram(connection, wallet);
  const ix = await program.methods
    .closeRewardReceipt()
    .accounts({
      rewardReceipt: params.rewardReceiptId,
      receiptManager: params.receiptManagerId,
      authority: wallet.publicKey,
    })
    .instruction();
  transaction.add(ix);
  return transaction;
};

export const withSetRewardReceiptAllowed = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  params: {
    receiptManagerId: PublicKey;
    rewardReceiptId: PublicKey;
    auth: boolean;
  }
): Promise<Transaction> => {
  const program = receiptManagerProgram(connection, wallet);
  const ix = await program.methods
    .setRewardReceiptAllowed(params.auth)
    .accounts({
      receiptManager: params.receiptManagerId,
      rewardReceipt: params.rewardReceiptId,
      authority: wallet.publicKey,
    })
    .instruction();
  transaction.add(ix);
  return transaction;
};


