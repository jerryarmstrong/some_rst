hub/types/decoders/PublicKey.ts
===============================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import { PublicKey as _PublicKey } from '@solana/web3.js';
import { Type, success, failure, TypeOf } from 'io-ts';

export const PublicKey = new Type<_PublicKey, string, unknown>(
  'PublicKey',
  (u: unknown): u is _PublicKey => u instanceof _PublicKey,
  (input, context) => {
    try {
      if (typeof input === 'string') {
        const pk = new _PublicKey(input);
        return success(pk);
      } else {
        return failure(input, context);
      }
    } catch {
      return failure(input, context);
    }
  },
  (a: _PublicKey) => a.toBase58(),
);

export type PublicKey = TypeOf<typeof PublicKey>;


