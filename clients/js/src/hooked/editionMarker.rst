clients/js/src/hooked/editionMarker.ts
======================================

Last edited: 2023-08-11 07:39:15

Contents:

.. code-block:: ts

    import { Pda, PublicKey } from '@metaplex-foundation/umi';
import { findEditionMarkerPda } from '../generated';

export function findEditionMarkerPdaFromEditionNumber(
  context: Parameters<typeof findEditionMarkerPda>[0],
  seeds: {
    /** The address of the mint account */
    mint: PublicKey;
    /** The edition number. */
    editionNumber: number | bigint;
  }
): Pda {
  return findEditionMarkerPda(context, {
    mint: seeds.mint,
    editionMarker: (BigInt(seeds.editionNumber) / 248n).toString(10),
  });
}


