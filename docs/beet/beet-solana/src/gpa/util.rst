beet-solana/src/gpa/util.ts
===========================

Last edited: 2022-09-21 01:30:08

Contents:

.. code-block:: ts

    import { FixedSizeBeet } from '@metaplex-foundation/beet'
import base58 from 'bs58'

export function encodeFixedBeet<T>(beet: FixedSizeBeet<T>, val: T) {
  const buf = Buffer.alloc(beet.byteSize)
  beet.write(buf, 0, val)
  return base58.encode(buf)
}


