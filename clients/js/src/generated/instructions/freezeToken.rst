clients/js/src/generated/instructions/freezeToken.ts
====================================================

Last edited: 2023-06-19 17:40:55

Contents:

.. code-block:: ts

    /**
 * This code was AUTOGENERATED using the kinobi library.
 * Please DO NOT EDIT THIS FILE, instead use visitors
 * to add features, then rerun kinobi to update it.
 *
 * @see https://github.com/metaplex-foundation/kinobi
 */

import {
  AccountMeta,
  Context,
  Pda,
  PublicKey,
  Signer,
  TransactionBuilder,
  transactionBuilder,
} from '@metaplex-foundation/umi';
import {
  Serializer,
  mapSerializer,
  struct,
  u8,
} from '@metaplex-foundation/umi/serializers';
import { addAccountMeta } from '../shared';

// Accounts.
export type FreezeTokenInstructionAccounts = {
  account: PublicKey | Pda;
  mint: PublicKey | Pda;
  owner: Signer;
};

// Data.
export type FreezeTokenInstructionData = { discriminator: number };

export type FreezeTokenInstructionDataArgs = {};

/** @deprecated Use `getFreezeTokenInstructionDataSerializer()` without any argument instead. */
export function getFreezeTokenInstructionDataSerializer(
  _context: object
): Serializer<FreezeTokenInstructionDataArgs, FreezeTokenInstructionData>;
export function getFreezeTokenInstructionDataSerializer(): Serializer<
  FreezeTokenInstructionDataArgs,
  FreezeTokenInstructionData
>;
export function getFreezeTokenInstructionDataSerializer(
  _context: object = {}
): Serializer<FreezeTokenInstructionDataArgs, FreezeTokenInstructionData> {
  return mapSerializer<
    FreezeTokenInstructionDataArgs,
    any,
    FreezeTokenInstructionData
  >(
    struct<FreezeTokenInstructionData>([['discriminator', u8()]], {
      description: 'FreezeTokenInstructionData',
    }),
    (value) => ({ ...value, discriminator: 10 })
  ) as Serializer<FreezeTokenInstructionDataArgs, FreezeTokenInstructionData>;
}

// Instruction.
export function freezeToken(
  context: Pick<Context, 'programs'>,
  input: FreezeTokenInstructionAccounts
): TransactionBuilder {
  const signers: Signer[] = [];
  const keys: AccountMeta[] = [];

  // Program ID.
  const programId = context.programs.getPublicKey(
    'splToken',
    'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA'
  );

  // Resolved inputs.
  const resolvedAccounts = {
    account: [input.account, true] as const,
    mint: [input.mint, false] as const,
    owner: [input.owner, false] as const,
  };

  addAccountMeta(keys, signers, resolvedAccounts.account, false);
  addAccountMeta(keys, signers, resolvedAccounts.mint, false);
  addAccountMeta(keys, signers, resolvedAccounts.owner, false);

  // Data.
  const data = getFreezeTokenInstructionDataSerializer().serialize({});

  // Bytes Created On Chain.
  const bytesCreatedOnChain = 0;

  return transactionBuilder([
    { instruction: { keys, programId, data }, signers, bytesCreatedOnChain },
  ]);
}


