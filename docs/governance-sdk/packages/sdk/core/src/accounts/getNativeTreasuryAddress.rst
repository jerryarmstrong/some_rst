packages/sdk/core/src/accounts/getNativeTreasuryAddress.ts
==========================================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import { PublicKey } from '@solana/web3.js';

/**
 * Get the address for a Native Treasury
 */
export async function getNativeTreasuryAddress(programId: PublicKey, governance: PublicKey) {
  const [signatoryRecordAddress] = await PublicKey.findProgramAddress(
    [Buffer.from('native-treasury'), governance.toBuffer()],
    programId
  );

  return signatoryRecordAddress;
}


