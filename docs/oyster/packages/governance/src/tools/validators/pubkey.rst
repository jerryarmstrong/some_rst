packages/governance/src/tools/validators/pubkey.ts
==================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { coerce, instance, string } from 'superstruct';
import { PublicKey } from '@solana/web3.js';

export const PublicKeyFromString = coerce(
  instance(PublicKey),
  string(),
  value => new PublicKey(value),
);


