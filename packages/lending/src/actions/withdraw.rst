packages/lending/src/actions/withdraw.tsx
=========================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import {  WalletNotConnectedError } from "@solana/wallet-adapter-base";
import {
  Account,
  Connection,
  PublicKey,
  TransactionInstruction,
} from '@solana/web3.js';
import { contexts, utils, actions, models, TokenAccount, WalletSigner } from '@oyster/common';
import {
  accrueInterestInstruction,
  LendingReserve,
  withdrawInstruction,
} from './../models/lending';
import { AccountLayout } from '@solana/spl-token';

const { approve } = models;
const { findOrCreateAccountByMint } = actions;
const { sendTransaction } = contexts.Connection;
const { LENDING_PROGRAM_ID, notify } = utils;

export const withdraw = async (
  from: TokenAccount, // CollateralAccount
  amountLamports: number, // in collateral token (lamports)
  reserve: LendingReserve,
  reserveAddress: PublicKey,
  connection: Connection,
  wallet: WalletSigner,
) => {
  if (!wallet.publicKey) throw new WalletNotConnectedError();

  notify({
    message: 'Withdrawing funds...',
    description: 'Please review transactions to approve.',
    type: 'warn',
  });

  // user from account
  const signers: Account[] = [];
  const instructions: TransactionInstruction[] = [];
  const cleanupInstructions: TransactionInstruction[] = [];

  const accountRentExempt = await connection.getMinimumBalanceForRentExemption(
    AccountLayout.span,
  );

  const [authority] = await PublicKey.findProgramAddress(
    [reserve.lendingMarket.toBuffer()],
    LENDING_PROGRAM_ID,
  );

  const fromAccount = from.pubkey;

  // create approval for transfer transactions
  const transferAuthority = approve(
    instructions,
    cleanupInstructions,
    fromAccount,
    wallet.publicKey,
    amountLamports,
  );

  signers.push(transferAuthority);

  // get destination account
  const toAccount = await findOrCreateAccountByMint(
    wallet.publicKey,
    wallet.publicKey,
    instructions,
    cleanupInstructions,
    accountRentExempt,
    reserve.liquidityMint,
    signers,
  );

  instructions.push(accrueInterestInstruction(reserveAddress));

  instructions.push(
    withdrawInstruction(
      amountLamports,
      fromAccount,
      toAccount,
      reserveAddress,
      reserve.collateralMint,
      reserve.liquiditySupply,
      reserve.lendingMarket,
      authority,
      transferAuthority.publicKey,
    ),
  );

  try {
    let { txid }  = await sendTransaction(
      connection,
      wallet,
      instructions.concat(cleanupInstructions),
      signers,
      true,
    );

    notify({
      message: 'Funds deposited.',
      type: 'success',
      description: `Transaction - ${txid}`,
    });
  } catch {
    // TODO:
  }
};


