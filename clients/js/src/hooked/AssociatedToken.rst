clients/js/src/hooked/AssociatedToken.ts
========================================

Last edited: 2023-06-19 17:40:55

Contents:

.. code-block:: ts

    import { Context, Pda, PublicKey } from '@metaplex-foundation/umi';
import { publicKey } from '@metaplex-foundation/umi/serializers';

export function findAssociatedTokenPda(
  context: Pick<Context, 'eddsa' | 'programs'>,
  seeds: {
    /** The address of the mint account */
    mint: PublicKey;
    /** The owner of the token account */
    owner: PublicKey;
  }
): Pda {
  const associatedTokenProgramId =
    context.programs.getPublicKey('splAssociatedToken');
  const tokenProgramId = context.programs.getPublicKey('splToken');
  return context.eddsa.findPda(associatedTokenProgramId, [
    publicKey().serialize(seeds.owner),
    publicKey().serialize(tokenProgramId),
    publicKey().serialize(seeds.mint),
  ]);
}


