clients/js/src/generated/instructions/createAccount.ts
======================================================

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
  PublicKey,
  Signer,
  SolAmount,
  TransactionBuilder,
  mapAmountSerializer,
  transactionBuilder,
} from '@metaplex-foundation/umi';
import {
  Serializer,
  mapSerializer,
  publicKey as publicKeySerializer,
  struct,
  u32,
  u64,
} from '@metaplex-foundation/umi/serializers';
import { addAccountMeta, addObjectProperty } from '../shared';

// Accounts.
export type CreateAccountInstructionAccounts = {
  payer?: Signer;
  newAccount: Signer;
};

// Data.
export type CreateAccountInstructionData = {
  discriminator: number;
  lamports: SolAmount;
  space: bigint;
  programId: PublicKey;
};

export type CreateAccountInstructionDataArgs = {
  lamports: SolAmount;
  space: number | bigint;
  programId: PublicKey;
};

/** @deprecated Use `getCreateAccountInstructionDataSerializer()` without any argument instead. */
export function getCreateAccountInstructionDataSerializer(
  _context: object
): Serializer<CreateAccountInstructionDataArgs, CreateAccountInstructionData>;
export function getCreateAccountInstructionDataSerializer(): Serializer<
  CreateAccountInstructionDataArgs,
  CreateAccountInstructionData
>;
export function getCreateAccountInstructionDataSerializer(
  _context: object = {}
): Serializer<CreateAccountInstructionDataArgs, CreateAccountInstructionData> {
  return mapSerializer<
    CreateAccountInstructionDataArgs,
    any,
    CreateAccountInstructionData
  >(
    struct<CreateAccountInstructionData>(
      [
        ['discriminator', u32()],
        ['lamports', mapAmountSerializer(u64(), 'SOL', 9)],
        ['space', u64()],
        ['programId', publicKeySerializer()],
      ],
      { description: 'CreateAccountInstructionData' }
    ),
    (value) => ({ ...value, discriminator: 0 })
  ) as Serializer<
    CreateAccountInstructionDataArgs,
    CreateAccountInstructionData
  >;
}

// Args.
export type CreateAccountInstructionArgs = CreateAccountInstructionDataArgs;

// Instruction.
export function createAccount(
  context: Pick<Context, 'programs' | 'payer'>,
  input: CreateAccountInstructionAccounts & CreateAccountInstructionArgs
): TransactionBuilder {
  const signers: Signer[] = [];
  const keys: AccountMeta[] = [];

  // Program ID.
  const programId = context.programs.getPublicKey(
    'splSystem',
    '11111111111111111111111111111111'
  );

  // Resolved inputs.
  const resolvedAccounts = {
    newAccount: [input.newAccount, true] as const,
  };
  const resolvingArgs = {};
  addObjectProperty(
    resolvedAccounts,
    'payer',
    input.payer
      ? ([input.payer, true] as const)
      : ([context.payer, true] as const)
  );
  const resolvedArgs = { ...input, ...resolvingArgs };

  addAccountMeta(keys, signers, resolvedAccounts.payer, false);
  addAccountMeta(keys, signers, resolvedAccounts.newAccount, false);

  // Data.
  const data =
    getCreateAccountInstructionDataSerializer().serialize(resolvedArgs);

  // Bytes Created On Chain.
  const bytesCreatedOnChain = Number(input.space) + ACCOUNT_HEADER_SIZE;

  return transactionBuilder([
    { instruction: { keys, programId, data }, signers, bytesCreatedOnChain },
  ]);
}


