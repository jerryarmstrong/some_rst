beet-solana/src/beet-solana.ts
==============================

Last edited: 2022-09-21 01:30:08

Contents:

.. code-block:: ts

    import { SupportedTypeDefinition } from '@metaplex-foundation/beet'
import { KeysExports, keysTypeMap, KeysTypeMapKey } from './keys'

export * from './keys'
export * from './gpa'

/**
 * @category TypeDefinition
 */
export type BeetSolanaTypeMapKey = KeysTypeMapKey
/**
 * @category TypeDefinition
 */
export type BeetSolanaExports = KeysExports

/**
 * Maps solana beet exports to metadata which describes in which package it
 * is defined as well as which TypeScript type is used to represent the
 * deserialized value in JavaScript.
 *
 * @category TypeDefinition
 */
export const supportedTypeMap: Record<
  BeetSolanaTypeMapKey,
  SupportedTypeDefinition & {
    beet: BeetSolanaExports
  }
> = keysTypeMap


