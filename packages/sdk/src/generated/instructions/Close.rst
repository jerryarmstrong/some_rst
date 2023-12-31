packages/sdk/src/generated/instructions/Close.ts
================================================

Last edited: 2023-06-14 20:00:41

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
 * @category Close
 * @category generated
 */
export const CloseStruct = new beet.BeetArgsStruct<{ instructionDiscriminator: number }>(
  [['instructionDiscriminator', beet.u8]],
  'CloseInstructionArgs',
);
/**
 * Accounts required by the _Close_ instruction
 *
 * @property [_writable_, **signer**] authority The collection authority
 * @property [_writable_] migrationState The migration state account
 * @category Instructions
 * @category Close
 * @category generated
 */
export type CloseInstructionAccounts = {
  authority: web3.PublicKey;
  migrationState: web3.PublicKey;
  systemProgram?: web3.PublicKey;
};

export const closeInstructionDiscriminator = 1;

/**
 * Creates a _Close_ instruction.
 *
 * @param accounts that will be accessed while the instruction is processed
 * @category Instructions
 * @category Close
 * @category generated
 */
export function createCloseInstruction(
  accounts: CloseInstructionAccounts,
  programId = new web3.PublicKey('migrxZFChTqicHpNa1CAjPcF29Mui2JU2q4Ym7qQUTi'),
) {
  const [data] = CloseStruct.serialize({
    instructionDiscriminator: closeInstructionDiscriminator,
  });
  const keys: web3.AccountMeta[] = [
    {
      pubkey: accounts.authority,
      isWritable: true,
      isSigner: true,
    },
    {
      pubkey: accounts.migrationState,
      isWritable: true,
      isSigner: false,
    },
    {
      pubkey: accounts.systemProgram ?? web3.SystemProgram.programId,
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


