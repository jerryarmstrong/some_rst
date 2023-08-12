clients/js/src/hooked/candyMachineAuthority.ts
==============================================

Last edited: 2023-08-11 23:25:39

Contents:

.. code-block:: ts

    import { Context, Pda, PublicKey } from '@metaplex-foundation/umi';
import { publicKey, string } from '@metaplex-foundation/umi/serializers';

export function findCandyMachineAuthorityPda(
  context: Pick<Context, 'eddsa' | 'programs'>,
  seeds: {
    /** The Candy Machine address */
    candyMachine: PublicKey;
  }
): Pda {
  const programId = context.programs.get('mplCandyMachineCore').publicKey;
  return context.eddsa.findPda(programId, [
    string({ size: 'variable' }).serialize('candy_machine'),
    publicKey().serialize(seeds.candyMachine),
  ]);
}


