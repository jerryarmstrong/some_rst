src/util/publickey-to-name.js
=============================

Last edited: 2020-06-24 17:49:11

Contents:

.. code-block:: js

    import Haikunator from 'haikunator';
import type {PublicKey} from '@solana/web3.js';

export function publicKeyToName(publicKey: PublicKey): string {
  const haikunator = new Haikunator({
    seed: publicKey.toString(),
  });
  return haikunator.haikunate();
}


