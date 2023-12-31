clients/js-solita/src/generated/instructions/AddNoneConstraintToEscrowConstraintModel.ts
========================================================================================

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
import {
  AddNoneConstraintToEscrowConstraintModelArgs,
  addNoneConstraintToEscrowConstraintModelArgsBeet,
} from '../types/AddNoneConstraintToEscrowConstraintModelArgs';

/**
 * @category Instructions
 * @category AddNoneConstraintToEscrowConstraintModel
 * @category generated
 */
export type AddNoneConstraintToEscrowConstraintModelInstructionArgs = {
  addNoneConstraintToEscrowConstraintModelArgs: AddNoneConstraintToEscrowConstraintModelArgs;
};
/**
 * @category Instructions
 * @category AddNoneConstraintToEscrowConstraintModel
 * @category generated
 */
export const AddNoneConstraintToEscrowConstraintModelStruct = new beet.FixableBeetArgsStruct<
  AddNoneConstraintToEscrowConstraintModelInstructionArgs & {
    instructionDiscriminator: number;
  }
>(
  [
    ['instructionDiscriminator', beet.u8],
    [
      'addNoneConstraintToEscrowConstraintModelArgs',
      addNoneConstraintToEscrowConstraintModelArgsBeet,
    ],
  ],
  'AddNoneConstraintToEscrowConstraintModelInstructionArgs',
);
/**
 * Accounts required by the _AddNoneConstraintToEscrowConstraintModel_ instruction
 *
 * @property [_writable_] constraintModel Constraint model account
 * @property [_writable_, **signer**] payer Wallet paying for the transaction and new account, will be set as the creator of the constraint model
 * @property [**signer**] updateAuthority Update authority of the constraint model
 * @property [] sysvarInstructions Instructions sysvar account
 * @category Instructions
 * @category AddNoneConstraintToEscrowConstraintModel
 * @category generated
 */
export type AddNoneConstraintToEscrowConstraintModelInstructionAccounts = {
  constraintModel: web3.PublicKey;
  payer: web3.PublicKey;
  updateAuthority: web3.PublicKey;
  systemProgram?: web3.PublicKey;
  sysvarInstructions: web3.PublicKey;
};

export const addNoneConstraintToEscrowConstraintModelInstructionDiscriminator = 4;

/**
 * Creates a _AddNoneConstraintToEscrowConstraintModel_ instruction.
 *
 * @param accounts that will be accessed while the instruction is processed
 * @param args to provide as instruction data to the program
 *
 * @category Instructions
 * @category AddNoneConstraintToEscrowConstraintModel
 * @category generated
 */
export function createAddNoneConstraintToEscrowConstraintModelInstruction(
  accounts: AddNoneConstraintToEscrowConstraintModelInstructionAccounts,
  args: AddNoneConstraintToEscrowConstraintModelInstructionArgs,
  programId = new web3.PublicKey('trifMWutwBxkSuatmpPVnEe7NoE3BJKgjVi8sSyoXWX'),
) {
  const [data] = AddNoneConstraintToEscrowConstraintModelStruct.serialize({
    instructionDiscriminator: addNoneConstraintToEscrowConstraintModelInstructionDiscriminator,
    ...args,
  });
  const keys: web3.AccountMeta[] = [
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
      pubkey: accounts.updateAuthority,
      isWritable: false,
      isSigner: true,
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


