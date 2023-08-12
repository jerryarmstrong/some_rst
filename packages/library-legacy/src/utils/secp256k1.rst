packages/library-legacy/src/utils/secp256k1.ts
==============================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import {secp256k1} from '@noble/curves/secp256k1';

export const ecdsaSign = (
  msgHash: Parameters<typeof secp256k1.sign>[0],
  privKey: Parameters<typeof secp256k1.sign>[1],
) => {
  const signature = secp256k1.sign(msgHash, privKey);
  return [signature.toCompactRawBytes(), signature.recovery!] as const;
};
export const isValidPrivateKey = secp256k1.utils.isValidPrivateKey;
export const publicKeyCreate = secp256k1.getPublicKey;


