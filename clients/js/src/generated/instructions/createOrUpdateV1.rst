clients/js/src/generated/instructions/createOrUpdateV1.ts
=========================================================

Last edited: 2023-08-01 17:12:05

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
  none,
  transactionBuilder,
} from '@metaplex-foundation/umi';
import {
  Serializer,
  mapSerializer,
  struct,
  u8,
} from '@metaplex-foundation/umi/serializers';
import {
  RuleSetRevisionInput,
  RuleSetRevisionInputArgs,
  getRuleSetRevisionInputSerializer,
} from '../../hooked';
import { addAccountMeta, addObjectProperty } from '../shared';

// Accounts.
export type CreateOrUpdateV1InstructionAccounts = {
  /** Payer and creator of the RuleSet */
  payer?: Signer;
  /** The PDA account where the RuleSet is stored */
  ruleSetPda: PublicKey | Pda;
  /** System program */
  systemProgram?: PublicKey | Pda;
  /** The buffer to copy a complete ruleset from */
  bufferPda?: PublicKey | Pda;
};

// Data.
export type CreateOrUpdateV1InstructionData = {
  discriminator: number;
  createOrUpdateV1Discriminator: number;
  ruleSetRevision: RuleSetRevisionInput;
};

export type CreateOrUpdateV1InstructionDataArgs = {
  ruleSetRevision?: RuleSetRevisionInputArgs;
};

/** @deprecated Use `getCreateOrUpdateV1InstructionDataSerializer()` without any argument instead. */
export function getCreateOrUpdateV1InstructionDataSerializer(
  _context: object
): Serializer<
  CreateOrUpdateV1InstructionDataArgs,
  CreateOrUpdateV1InstructionData
>;
export function getCreateOrUpdateV1InstructionDataSerializer(): Serializer<
  CreateOrUpdateV1InstructionDataArgs,
  CreateOrUpdateV1InstructionData
>;
export function getCreateOrUpdateV1InstructionDataSerializer(
  _context: object = {}
): Serializer<
  CreateOrUpdateV1InstructionDataArgs,
  CreateOrUpdateV1InstructionData
> {
  return mapSerializer<
    CreateOrUpdateV1InstructionDataArgs,
    any,
    CreateOrUpdateV1InstructionData
  >(
    struct<CreateOrUpdateV1InstructionData>(
      [
        ['discriminator', u8()],
        ['createOrUpdateV1Discriminator', u8()],
        ['ruleSetRevision', getRuleSetRevisionInputSerializer()],
      ],
      { description: 'CreateOrUpdateV1InstructionData' }
    ),
    (value) => ({
      ...value,
      discriminator: 0,
      createOrUpdateV1Discriminator: 0,
      ruleSetRevision: value.ruleSetRevision ?? none(),
    })
  ) as Serializer<
    CreateOrUpdateV1InstructionDataArgs,
    CreateOrUpdateV1InstructionData
  >;
}

// Args.
export type CreateOrUpdateV1InstructionArgs =
  CreateOrUpdateV1InstructionDataArgs;

// Instruction.
export function createOrUpdateV1(
  context: Pick<Context, 'programs' | 'payer'>,
  input: CreateOrUpdateV1InstructionAccounts & CreateOrUpdateV1InstructionArgs
): TransactionBuilder {
  const signers: Signer[] = [];
  const keys: AccountMeta[] = [];

  // Program ID.
  const programId = context.programs.getPublicKey(
    'mplTokenAuthRules',
    'auth9SigNpDKz4sJJ1DfCTuZrZNSAgh9sFD3rboVmgg'
  );

  // Resolved inputs.
  const resolvedAccounts = {
    ruleSetPda: [input.ruleSetPda, true] as const,
  };
  const resolvingArgs = {};
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
    resolvedAccounts,
    'bufferPda',
    input.bufferPda
      ? ([input.bufferPda, false] as const)
      : ([programId, false] as const)
  );
  const resolvedArgs = { ...input, ...resolvingArgs };

  addAccountMeta(keys, signers, resolvedAccounts.payer, false);
  addAccountMeta(keys, signers, resolvedAccounts.ruleSetPda, false);
  addAccountMeta(keys, signers, resolvedAccounts.systemProgram, false);
  addAccountMeta(keys, signers, resolvedAccounts.bufferPda, false);

  // Data.
  const data =
    getCreateOrUpdateV1InstructionDataSerializer().serialize(resolvedArgs);

  // Bytes Created On Chain.
  const bytesCreatedOnChain = 0;

  return transactionBuilder([
    { instruction: { keys, programId, data }, signers, bytesCreatedOnChain },
  ]);
}


