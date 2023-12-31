packages/js/src/types/PublicKey.ts
==================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import { PublicKey, PublicKeyInitData } from '@solana/web3.js';

export { PublicKey } from '@solana/web3.js';
export type PublicKeyString = string;
export type PublicKeyValues =
  | PublicKeyInitData
  | { publicKey: PublicKey }
  | { address: PublicKey };

export const toPublicKey = (value: PublicKeyValues): PublicKey => {
  if (typeof value === 'object' && 'publicKey' in value) {
    return value.publicKey;
  }

  if (typeof value === 'object' && 'address' in value) {
    return (value as { address: PublicKey }).address;
  }

  return new PublicKey(value);
};


