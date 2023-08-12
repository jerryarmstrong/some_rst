packages/keys/src/key-pair.ts
=============================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { assertKeyGenerationIsAvailable } from '@solana/assertions';

export async function generateKeyPair(): Promise<CryptoKeyPair> {
    await assertKeyGenerationIsAvailable();
    const keyPair = await crypto.subtle.generateKey(
        /* algorithm */ 'Ed25519', // Native implementation status: https://github.com/WICG/webcrypto-secure-curves/issues/20
        /* extractable */ false, // Prevents the bytes of the private key from being visible to JS.
        /* allowed uses */ ['sign', 'verify']
    );
    return keyPair as CryptoKeyPair;
}


