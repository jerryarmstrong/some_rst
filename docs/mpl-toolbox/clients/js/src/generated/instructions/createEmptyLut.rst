clients/js/src/generated/instructions/createEmptyLut.ts
=======================================================

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
  ACCOUNT_HEADER_SIZE,
  AccountMeta,
  Context,
  Pda,
  PublicKey,
  Signer,
  TransactionBuilder,
  publicKey,
  transactionBuilder,
} from '@metaplex-foundation/umi';
import {
  Serializer,
  mapSerializer,
  struct,
  u32,
  u64,
  u8,
} from '@metaplex-foundation/umi/serializers';
import { findAddressLookupTablePda } from '../accounts';
import { PickPartial, addAccountMeta, addObjectProperty } from '../shared';

// Accounts.
export type CreateEmptyLutInstructionAccounts = {
  address?: Pda;
  authority?: Signer;
  payer?: Signer;
  systemProgram?: PublicKey | Pda;
};

// Data.
export type CreateEmptyLutInstructionData = {
  discriminator: number;
  recentSlot: bigint;
  bump: number;
};

export type CreateEmptyLutInstructionDataArgs = {
  recentSlot: number | bigint;
  bump: number;
};

/** @deprecated Use `getCreateEmptyLutInstructionDataSerializer()` without any argument instead. */
export function getCreateEmptyLutInstructionDataSerializer(
  _context: object
): Serializer<CreateEmptyLutInstructionDataArgs, CreateEmptyLutInstructionData>;
export function getCreateEmptyLutInstructionDataSerializer(): Serializer<
  CreateEmptyLutInstructionDataArgs,
  CreateEmptyLutInstructionData
>;
export function getCreateEmptyLutInstructionDataSerializer(
  _context: object = {}
): Serializer<
  CreateEmptyLutInstructionDataArgs,
  CreateEmptyLutInstructionData
> {
  return mapSerializer<
    CreateEmptyLutInstructionDataArgs,
    any,
    CreateEmptyLutInstructionData
  >(
    struct<CreateEmptyLutInstructionData>(
      [
        ['discriminator', u32()],
        ['recentSlot', u64()],
        ['bump', u8()],
      ],
      { description: 'CreateEmptyLutInstructionData' }
    ),
    (value) => ({ ...value, discriminator: 0 })
  ) as Serializer<
    CreateEmptyLutInstructionDataArgs,
    CreateEmptyLutInstructionData
  >;
}

// Args.
export type CreateEmptyLutInstructionArgs = PickPartial<
  CreateEmptyLutInstructionDataArgs,
  'bump'
>;

// Instruction.
export function createEmptyLut(
  context: Pick<Context, 'programs' | 'eddsa' | 'identity' | 'payer'>,
  input: CreateEmptyLutInstructionAccounts & CreateEmptyLutInstructionArgs
): TransactionBuilder {
  const signers: Signer[] = [];
  const keys: AccountMeta[] = [];

  // Program ID.
  const programId = context.programs.getPublicKey(
    'splAddressLookupTable',
    'AddressLookupTab1e1111111111111111111111111'
  );

  // Resolved inputs.
  const resolvedAccounts = {};
  const resolvingArgs = {};
  addObjectProperty(
    resolvedAccounts,
    'authority',
    input.authority
      ? ([input.authority, false] as const)
      : ([context.identity, false] as const)
  );
  addObjectProperty(
    resolvedAccounts,
    'address',
    input.address
      ? ([input.address, true] as const)
      : ([
          findAddressLookupTablePda(context, {
            authority: publicKey(resolvedAccounts.authority[0], false),
            recentSlot: input.recentSlot,
          }),
          true,
        ] as const)
  );
  addObjectProperty(
    resolvedAccounts,
    'payer',
    input.payer
      ? ([input.payer, true] as const)
      : ([context.payer, true] as const)
  );
  addObjectProperty(
    resolvedAccounts,
    'systemProgram',
    input.systemProgram
      ? ([input.systemProgram, false] as const)
      : ([
          context.programs.getPublicKey(
            'splSystem',
            '11111111111111111111111111111111'
          ),
          false,
        ] as const)
  );
  addObjectProperty(
    resolvingArgs,
    'bump',
    input.bump ?? resolvedAccounts.address[0][1]
  );
  const resolvedArgs = { ...input, ...resolvingArgs };

  addAccountMeta(keys, signers, resolvedAccounts.address, false);
  addAccountMeta(keys, signers, resolvedAccounts.authority, false);
  addAccountMeta(keys, signers, resolvedAccounts.payer, false);
  addAccountMeta(keys, signers, resolvedAccounts.systemProgram, false);

  // Data.
  const data =
    getCreateEmptyLutInstructionDataSerializer().serialize(resolvedArgs);

  // Bytes Created On Chain.
  const bytesCreatedOnChain = 56 + ACCOUNT_HEADER_SIZE;

  return transactionBuilder([
    { instruction: { keys, programId, data }, signers, bytesCreatedOnChain },
  ]);
}


