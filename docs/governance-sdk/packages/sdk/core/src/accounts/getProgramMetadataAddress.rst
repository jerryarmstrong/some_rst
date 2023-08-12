packages/sdk/core/src/accounts/getProgramMetadataAddress.ts
===========================================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import { PublicKey } from '@solana/web3.js';

/**
 * Get the address for a Program Metadata
 */
export async function getProgramMetadataAddress(programId: PublicKey) {
  const [signatoryRecordAddress] = await PublicKey.findProgramAddress(
    [Buffer.from('metadata')],
    programId
  );

  return signatoryRecordAddress;
}


