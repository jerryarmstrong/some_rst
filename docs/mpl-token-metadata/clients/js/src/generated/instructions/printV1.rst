clients/js/src/generated/instructions/printV1.ts
================================================

Last edited: 2023-08-11 07:39:15

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
  publicKey,
  transactionBuilder,
} from '@metaplex-foundation/umi';
import {
  Serializer,
  mapSerializer,
  struct,
  u64,
  u8,
} from '@metaplex-foundation/umi/serializers';
import { addAccountMeta, addObjectProperty } from '../shared';

// Accounts.
export type PrintV1InstructionAccounts = {
  /** New Metadata key (pda of ['metadata', program id, mint id]) */
  editionMetadata: PublicKey | Pda;
  /** New Edition (pda of ['metadata', program id, mint id, 'edition']) */
  edition: PublicKey | Pda;
  /** Mint of new token - THIS WILL TRANSFER AUTHORITY AWAY FROM THIS KEY */
  editionMint: PublicKey | Pda;
  /** Owner of the token account of new token */
  editionTokenAccountOwner: PublicKey | Pda;
  /** Token account of new token */
  editionTokenAccount: PublicKey | Pda;
  /** Mint authority of new mint */
  editionMintAuthority: Signer;
  /** Token record account */
  editionTokenRecord?: PublicKey | Pda;
  /** Master Record Edition V2 (pda of ['metadata', program id, master metadata mint id, 'edition']) */
  masterEdition: PublicKey | Pda;
  /** Edition pda to mark creation - will be checked for pre-existence. (pda of ['metadata', program id, master metadata mint id, 'edition', edition_number]) where edition_number is NOT the edition number you pass in args but actually edition_number = floor(edition/EDITION_MARKER_BIT_SIZE). */
  editionMarkerPda: PublicKey | Pda;
  /** payer */
  payer?: Signer;
  /** owner of token account containing master token */
  masterTokenAccountOwner: Signer;
  /** token account containing token from master metadata mint */
  masterTokenAccount: PublicKey | Pda;
  /** Master record metadata account */
  masterMetadata: PublicKey | Pda;
  /** The update authority of the master edition. */
  updateAuthority?: PublicKey | Pda;
  /** Token program */
  splTokenProgram?: PublicKey | Pda;
  /** SPL Associated Token Account program */
  splAtaProgram?: PublicKey | Pda;
  /** Instructions sysvar account */
  sysvarInstructions?: PublicKey | Pda;
  /** System program */
  systemProgram?: PublicKey | Pda;
};

// Data.
export type PrintV1InstructionData = {
  discriminator: number;
  printV1Discriminator: number;
  edition: bigint;
};

export type PrintV1InstructionDataArgs = { edition: number | bigint };

/** @deprecated Use `getPrintV1InstructionDataSerializer()` without any argument instead. */
export function getPrintV1InstructionDataSerializer(
  _context: object
): Serializer<PrintV1InstructionDataArgs, PrintV1InstructionData>;
export function getPrintV1InstructionDataSerializer(): Serializer<
  PrintV1InstructionDataArgs,
  PrintV1InstructionData
>;
export function getPrintV1InstructionDataSerializer(
  _context: object = {}
): Serializer<PrintV1InstructionDataArgs, PrintV1InstructionData> {
  return mapSerializer<PrintV1InstructionDataArgs, any, PrintV1InstructionData>(
    struct<PrintV1InstructionData>(
      [
        ['discriminator', u8()],
        ['printV1Discriminator', u8()],
        ['edition', u64()],
      ],
      { description: 'PrintV1InstructionData' }
    ),
    (value) => ({ ...value, discriminator: 55, printV1Discriminator: 0 })
  ) as Serializer<PrintV1InstructionDataArgs, PrintV1InstructionData>;
}

// Args.
export type PrintV1InstructionArgs = PrintV1InstructionDataArgs;

// Instruction.
export function printV1(
  context: Pick<Context, 'programs' | 'identity' | 'payer'>,
  accounts: PrintV1InstructionAccounts,
  args: PrintV1InstructionArgs
): TransactionBuilder {
  const signers: Signer[] = [];
  const keys: AccountMeta[] = [];

  // Program ID.
  const programId = context.programs.getPublicKey(
    'mplTokenMetadata',
    'metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s'
  );

  // Resolved inputs.
  const resolvedAccounts = {
    editionMetadata: [accounts.editionMetadata, true] as const,
    edition: [accounts.edition, true] as const,
    editionMint: [accounts.editionMint, true] as const,
    editionTokenAccountOwner: [
      accounts.editionTokenAccountOwner,
      false,
    ] as const,
    editionTokenAccount: [accounts.editionTokenAccount, true] as const,
    editionMintAuthority: [accounts.editionMintAuthority, false] as const,
    masterEdition: [accounts.masterEdition, true] as const,
    editionMarkerPda: [accounts.editionMarkerPda, true] as const,
    masterTokenAccountOwner: [accounts.masterTokenAccountOwner, false] as const,
    masterTokenAccount: [accounts.masterTokenAccount, false] as const,
    masterMetadata: [accounts.masterMetadata, false] as const,
  };
  const resolvingArgs = {};
  addObjectProperty(
    resolvedAccounts,
    'editionTokenRecord',
    accounts.editionTokenRecord
      ? ([accounts.editionTokenRecord, true] as const)
      : ([programId, false] as const)
  );
  addObjectProperty(
    resolvedAccounts,
    'payer',
    accounts.payer
      ? ([accounts.payer, true] as const)
      : ([context.payer, true] as const)
  );
  addObjectProperty(
    resolvedAccounts,
    'updateAuthority',
    accounts.updateAuthority
      ? ([accounts.updateAuthority, false] as const)
      : ([context.identity.publicKey, false] as const)
  );
  addObjectProperty(
    resolvedAccounts,
    'splTokenProgram',
    accounts.splTokenProgram
      ? ([accounts.splTokenProgram, false] as const)
      : ([
          context.programs.getPublicKey(
            'splToken',
            'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA'
          ),
          false,
        ] as const)
  );
  addObjectProperty(
    resolvedAccounts,
    'splAtaProgram',
    accounts.splAtaProgram
      ? ([accounts.splAtaProgram, false] as const)
      : ([
          context.programs.getPublicKey(
            'splAssociatedToken',
            'ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL'
          ),
          false,
        ] as const)
  );
  addObjectProperty(
    resolvedAccounts,
    'sysvarInstructions',
    accounts.sysvarInstructions
      ? ([accounts.sysvarInstructions, false] as const)
      : ([
          publicKey('Sysvar1nstructions1111111111111111111111111'),
          false,
        ] as const)
  );
  addObjectProperty(
    resolvedAccounts,
    'systemProgram',
    accounts.systemProgram
      ? ([accounts.systemProgram, false] as const)
      : ([
          context.programs.getPublicKey(
            'splSystem',
            '11111111111111111111111111111111'
          ),
          false,
        ] as const)
  );
  const resolvedArgs = { ...args, ...resolvingArgs };

  addAccountMeta(keys, signers, resolvedAccounts.editionMetadata, false);
  addAccountMeta(keys, signers, resolvedAccounts.edition, false);
  addAccountMeta(keys, signers, resolvedAccounts.editionMint, false);
  addAccountMeta(
    keys,
    signers,
    resolvedAccounts.editionTokenAccountOwner,
    false
  );
  addAccountMeta(keys, signers, resolvedAccounts.editionTokenAccount, false);
  addAccountMeta(keys, signers, resolvedAccounts.editionMintAuthority, false);
  addAccountMeta(keys, signers, resolvedAccounts.editionTokenRecord, false);
  addAccountMeta(keys, signers, resolvedAccounts.masterEdition, false);
  addAccountMeta(keys, signers, resolvedAccounts.editionMarkerPda, false);
  addAccountMeta(keys, signers, resolvedAccounts.payer, false);
  addAccountMeta(
    keys,
    signers,
    resolvedAccounts.masterTokenAccountOwner,
    false
  );
  addAccountMeta(keys, signers, resolvedAccounts.masterTokenAccount, false);
  addAccountMeta(keys, signers, resolvedAccounts.masterMetadata, false);
  addAccountMeta(keys, signers, resolvedAccounts.updateAuthority, false);
  addAccountMeta(keys, signers, resolvedAccounts.splTokenProgram, false);
  addAccountMeta(keys, signers, resolvedAccounts.splAtaProgram, false);
  addAccountMeta(keys, signers, resolvedAccounts.sysvarInstructions, false);
  addAccountMeta(keys, signers, resolvedAccounts.systemProgram, false);

  // Data.
  const data = getPrintV1InstructionDataSerializer().serialize(resolvedArgs);

  // Bytes Created On Chain.
  const bytesCreatedOnChain = 0;

  return transactionBuilder([
    { instruction: { keys, programId, data }, signers, bytesCreatedOnChain },
  ]);
}


