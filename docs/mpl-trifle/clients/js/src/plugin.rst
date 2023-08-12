clients/js/src/plugin.ts
========================

Last edited: 2023-07-13 14:48:42

Contents:

.. code-block:: ts

    import { mplTokenMetadata } from '@metaplex-foundation/mpl-token-metadata';
import { UmiPlugin } from '@metaplex-foundation/umi';
import { createMplTrifleProgram } from './generated';

export const mplTrifle = (): UmiPlugin => ({
  install(umi) {
    umi.use(mplTokenMetadata());
    umi.programs.add(createMplTrifleProgram(), false);
  },
});


