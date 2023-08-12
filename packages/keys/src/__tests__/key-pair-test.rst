packages/keys/src/__tests__/key-pair-test.ts
============================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { generateKeyPair } from '../key-pair';

describe('generateKeyPair', () => {
    it.each(['private', 'public'])('generates an ed25519 %s `CryptoKey`', async type => {
        expect.assertions(1);
        const keyPair = await generateKeyPair();
        expect(keyPair).toMatchObject({
            [`${type}Key`]: expect.objectContaining({
                [Symbol.toStringTag]: 'CryptoKey',
                algorithm: { name: 'Ed25519' },
                type,
            }),
        });
    });
    it('generates a non-extractable private key', async () => {
        expect.assertions(1);
        const { privateKey } = await generateKeyPair();
        expect(privateKey).toHaveProperty('extractable', false);
    });
    it('generates a private key usable for signing operations', async () => {
        expect.assertions(1);
        const { privateKey } = await generateKeyPair();
        expect(privateKey).toHaveProperty('usages', ['sign']);
    });
    it('generates an extractable public key', async () => {
        expect.assertions(1);
        const { publicKey } = await generateKeyPair();
        expect(publicKey).toHaveProperty('extractable', true);
    });
    it('generates a public key usable for verifying signatures', async () => {
        expect.assertions(1);
        const { publicKey } = await generateKeyPair();
        expect(publicKey).toHaveProperty('usages', ['verify']);
    });
});


