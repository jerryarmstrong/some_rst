clients/js/src/hooked/mintAuthority.ts
======================================

Last edited: 2023-08-12 00:00:44

Contents:

.. code-block:: ts

    import { Context, Pda, PublicKey } from '@metaplex-foundation/umi';
import { publicKey } from '@metaplex-foundation/umi/serializers';
import { MPL_BUBBLEGUM_PROGRAM_ID } from '../generated';

export function findMintAuthorityPda(
  context: Pick<Context, 'programs' | 'eddsa'>,
  seeds: { mint: PublicKey }
): Pda {
  const programId = context.programs.getPublicKey(
    'mplBubblegum',
    MPL_BUBBLEGUM_PROGRAM_ID
  );
  return context.eddsa.findPda(programId, [publicKey().serialize(seeds.mint)]);
}


