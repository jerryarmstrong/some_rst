packages/umi-web3js-adapters/src/PublicKey.ts
=============================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    import { PublicKey } from '@metaplex-foundation/umi';
import { PublicKey as Web3JsPublicKey } from '@solana/web3.js';

export function fromWeb3JsPublicKey(publicKey: Web3JsPublicKey): PublicKey {
  return publicKey.toBase58() as PublicKey;
}

export function toWeb3JsPublicKey(publicKey: PublicKey): Web3JsPublicKey {
  return new Web3JsPublicKey(publicKey);
}


