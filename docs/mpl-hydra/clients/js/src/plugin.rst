clients/js/src/plugin.ts
========================

Last edited: 2023-06-19 18:36:17

Contents:

.. code-block:: ts

    import { UmiPlugin } from '@metaplex-foundation/umi';
import { mplToolbox } from '@metaplex-foundation/mpl-toolbox';
import { createMplHydraProgram } from './generated';

export const mplHydra = (): UmiPlugin => ({
  install(umi) {
    umi.use(mplToolbox());
    umi.programs.add(createMplHydraProgram(), false);
  },
});


