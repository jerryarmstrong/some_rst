clients/js/src/generated/instructions/initializeToken3.ts
=========================================================

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
  publicKey as publicKeySerializer,
  struct,
  u8,
} from '@metaplex-foundation/umi/serializers';
import { addAccountMeta } from '../shared';

// Accounts.
export type InitializeToken3InstructionAccounts = {
  account: PublicKey | Pda;
  mint: PublicKey | Pda;
};

// Data.
export type InitializeToken3InstructionData = {
  discriminator: number;
  owner: PublicKey;
};

export type InitializeToken3InstructionDataArgs = { owner: PublicKey };

/** @deprecated Use `getInitializeToken3InstructionDataSerializer()` without any argument instead. */
export function getInitializeToken3InstructionDataSerializer(
  _context: object
): Serializer<
  InitializeToken3InstructionDataArgs,
  InitializeToken3InstructionData
>;
export function getInitializeToken3InstructionDataSerializer(): Serializer<
  InitializeToken3InstructionDataArgs,
  InitializeToken3InstructionData
>;
export function getInitializeToken3InstructionDataSerializer(
  _context: object = {}
): Serializer<
  InitializeToken3InstructionDataArgs,
  InitializeToken3InstructionData
> {
  return mapSerializer<
    InitializeToken3InstructionDataArgs,
    any,
    InitializeToken3InstructionData
  >(
    struct<InitializeToken3InstructionData>(
      [
        ['discriminator', u8()],
        ['owner', publicKeySerializer()],
      ],
      { description: 'InitializeToken3InstructionData' }
    ),
    (value) => ({ ...value, discriminator: 18 })
  ) as Serializer<
    InitializeToken3InstructionDataArgs,
    InitializeToken3InstructionData
  >;
}

// Args.
export type InitializeToken3InstructionArgs =
  InitializeToken3InstructionDataArgs;

// Instruction.
export function initializeToken3(
  context: Pick<Context, 'programs'>,
  input: InitializeToken3InstructionAccounts & InitializeToken3InstructionArgs
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
  };
  const resolvingArgs = {};
  const resolvedArgs = { ...input, ...resolvingArgs };

  addAccountMeta(keys, signers, resolvedAccounts.account, false);
  addAccountMeta(keys, signers, resolvedAccounts.mint, false);

  // Data.
  const data =
    getInitializeToken3InstructionDataSerializer().serialize(resolvedArgs);

  // Bytes Created On Chain.
  const bytesCreatedOnChain = 0;

  return transactionBuilder([
    { instruction: { keys, programId, data }, signers, bytesCreatedOnChain },
  ]);
}


