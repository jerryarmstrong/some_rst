packages/addresses/src/public-key.ts
====================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { assertKeyExporterIsAvailable } from '@solana/assertions';

import { Base58EncodedAddress, getBase58EncodedAddressCodec } from './base58';

export async function getBase58EncodedAddressFromPublicKey(publicKey: CryptoKey): Promise<Base58EncodedAddress> {
    await assertKeyExporterIsAvailable();
    if (publicKey.type !== 'public' || publicKey.algorithm.name !== 'Ed25519') {
        // TODO: Coded error.
        throw new Error('The `CryptoKey` must be an `Ed25519` public key');
    }
    const publicKeyBytes = await crypto.subtle.exportKey('raw', publicKey);
    const [base58EncodedAddress] = getBase58EncodedAddressCodec().deserialize(new Uint8Array(publicKeyBytes));
    return base58EncodedAddress;
}


