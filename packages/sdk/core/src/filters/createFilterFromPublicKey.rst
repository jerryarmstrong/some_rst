packages/sdk/core/src/filters/createFilterFromPublicKey.ts
==========================================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import type { MemcmpFilter, PublicKey } from '@solana/web3.js';

/**
 * Convert a public key into a Memory Compare filter
 */
export function createFilterFromPublicKey(offset: number, pk: PublicKey): MemcmpFilter {
  return {
    memcmp: {
      offset,
      bytes: pk.toBase58(),
    },
  };
}


