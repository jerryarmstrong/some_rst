clients/js-solita/src/generated/instructions/CreateTrifleAccount.ts
===================================================================

Last edited: 2023-07-13 14:48:42

Contents:

.. code-block:: ts

    /**
 * This code was GENERATED using the solita package.
 * Please DO NOT EDIT THIS FILE, instead rerun solita to update it or write a wrapper to add functionality.
 *
 * See: https://github.com/metaplex-foundation/solita
 */

import * as beet from '@metaplex-foundation/beet';
import * as web3 from '@solana/web3.js';

/**
 * @category Instructions
 * @category CreateTrifleAccount
 * @category generated
 */
export const CreateTrifleAccountStruct = new beet.BeetArgsStruct<{
  instructionDiscriminator: number;
}>([['instructionDiscriminator', beet.u8]], 'CreateTrifleAccountInstructionArgs');
/**
 * Accounts required by the _CreateTrifleAccount_ instruction
 *
 * @property [_writable_] escrow Escrow account
 * @property [_writable_] metadata Metadata account
 * @property [] mint Mint account
 * @property [_writable_] tokenAccount Token account (base token)
 * @property [] edition Edition account
 * @property [_writable_] trifleAccount Trifle account
 * @property [**signer**] trifleAuthority Trifle Authority - the account that can sign transactions for the trifle account
 * @property [_writable_] constraintModel Escrow constraint model
 * @property [_writable_, **signer**] payer Wallet paying for the transaction
 * @property [] tokenMetadataProgram Token Metadata program
 * @property [] sysvarInstructions Instructions sysvar account
 * @category Instructions
 * @category CreateTrifleAccount
 * @category generated
 */
export type CreateTrifleAccountInstructionAccounts = {
  escrow: web3.PublicKey;
  metadata: web3.PublicKey;
  mint: web3.PublicKey;
  tokenAccount: web3.PublicKey;
  edition: web3.PublicKey;
  trifleAccount: web3.PublicKey;
  trifleAuthority: web3.PublicKey;
  constraintModel: web3.PublicKey;
  payer: web3.PublicKey;
  tokenMetadataProgram: web3.PublicKey;
  systemProgram?: web3.PublicKey;
  sysvarInstructions: web3.PublicKey;
};

export const createTrifleAccountInstructionDiscriminator = 1;

/**
 * Creates a _CreateTrifleAccount_ instruction.
 *
 * @param accounts that will be accessed while the instruction is processed
 * @category Instructions
 * @category CreateTrifleAccount
 * @category generated
 */
export function createCreateTrifleAccountInstruction(
  accounts: CreateTrifleAccountInstructionAccounts,
  programId = new web3.PublicKey('trifMWutwBxkSuatmpPVnEe7NoE3BJKgjVi8sSyoXWX'),
) {
  const [data] = CreateTrifleAccountStruct.serialize({
    instructionDiscriminator: createTrifleAccountInstructionDiscriminator,
  });
  const keys: web3.AccountMeta[] = [
    {
      pubkey: accounts.escrow,
      isWritable: true,
      isSigner: false,
    },
    {
      pubkey: accounts.metadata,
      isWritable: true,
      isSigner: false,
    },
    {
      pubkey: accounts.mint,
      isWritable: false,
      isSigner: false,
    },
    {
      pubkey: accounts.tokenAccount,
      isWritable: true,
      isSigner: false,
    },
    {
      pubkey: accounts.edition,
      isWritable: false,
      isSigner: false,
    },
    {
      pubkey: accounts.trifleAccount,
      isWritable: true,
      isSigner: false,
    },
    {
      pubkey: accounts.trifleAuthority,
      isWritable: false,
      isSigner: true,
    },
    {
      pubkey: accounts.constraintModel,
      isWritable: true,
      isSigner: false,
    },
    {
      pubkey: accounts.payer,
      isWritable: true,
      isSigner: true,
    },
    {
      pubkey: accounts.tokenMetadataProgram,
      isWritable: false,
      isSigner: false,
    },
    {
      pubkey: accounts.systemProgram ?? web3.SystemProgram.programId,
      isWritable: false,
      isSigner: false,
    },
    {
      pubkey: accounts.sysvarInstructions,
      isWritable: false,
      isSigner: false,
    },
  ];

  const ix = new web3.TransactionInstruction({
    programId,
    keys,
    data,
  });
  return ix;
}


