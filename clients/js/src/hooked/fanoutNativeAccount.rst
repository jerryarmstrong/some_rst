clients/js/src/hooked/fanoutNativeAccount.ts
============================================

Last edited: 2023-06-19 18:36:17

Contents:

.. code-block:: ts

    import { Context, Pda, PublicKey } from '@metaplex-foundation/umi';
import { publicKey, string } from '@metaplex-foundation/umi/serializers';

export function findFanoutNativeAccountPda(
  context: Pick<Context, 'eddsa' | 'programs'>,
  seeds: {
    /** The address of the fanout account */
    fanout: PublicKey;
  }
): Pda {
  const programId: PublicKey = context.programs.get('mplHydra').publicKey;
  return context.eddsa.findPda(programId, [
    string({ size: 'variable' }).serialize('fanout-native-account'),
    publicKey().serialize(seeds.fanout),
  ]);
}


