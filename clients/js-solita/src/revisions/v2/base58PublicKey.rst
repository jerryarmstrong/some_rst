clients/js-solita/src/revisions/v2/base58PublicKey.ts
=====================================================

Last edited: 2023-08-01 17:12:05

Contents:

.. code-block:: ts

    import type { PublicKey } from '@solana/web3.js';

export type Base58PublicKey = string;

export const toBase58PublicKey = (publicKey: PublicKey | string): Base58PublicKey => {
  return typeof publicKey === 'string' ? publicKey : publicKey.toBase58();
};


