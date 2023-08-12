app/validators/pubkey.ts
========================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: ts

    import { PublicKey } from '@solana/web3.js';
import { coerce, instance, string } from 'superstruct';

export const PublicKeyFromString = coerce(instance(PublicKey), string(), value => new PublicKey(value));


