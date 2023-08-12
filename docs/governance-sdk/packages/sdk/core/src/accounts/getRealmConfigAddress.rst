packages/sdk/core/src/accounts/getRealmConfigAddress.ts
=======================================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import { PublicKey } from '@solana/web3.js';

/**
 * Get the address for a Realm Config
 */
export async function getRealmConfigAddress(programId: PublicKey, realm: PublicKey) {
  const [realmConfigAddress] = await PublicKey.findProgramAddress(
    [Buffer.from('realm-config'), realm.toBuffer()],
    programId
  );

  return realmConfigAddress;
}


