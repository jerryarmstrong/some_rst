packages/sdk/test/utils/pdas.ts
===============================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: ts

    import { PublicKey } from '@solana/web3.js';
import { PROGRAM_ID } from '../../src/generated';
import { PROGRAM_ID as TOKEN_METADATA_ID } from '@metaplex-foundation/mpl-token-metadata';

export function findMigrationState(collectionMint: PublicKey): PublicKey {
  return PublicKey.findProgramAddressSync(
    [Buffer.from('migration'), collectionMint.toBuffer()],
    PROGRAM_ID,
  )[0];
}

export function findMetadataAddress(collectionMint: PublicKey): PublicKey {
  return PublicKey.findProgramAddressSync(
    [Buffer.from('metadata'), TOKEN_METADATA_ID.toBuffer(), collectionMint.toBuffer()],
    TOKEN_METADATA_ID,
  )[0];
}

export function findEditionAddress(collectionMint: PublicKey): PublicKey {
  return PublicKey.findProgramAddressSync(
    [
      Buffer.from('metadata'),
      TOKEN_METADATA_ID.toBuffer(),
      collectionMint.toBuffer(),
      Buffer.from('edition'),
    ],
    TOKEN_METADATA_ID,
  )[0];
}


