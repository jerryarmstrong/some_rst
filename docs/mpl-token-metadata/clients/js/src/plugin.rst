clients/js/src/plugin.ts
========================

Last edited: 2023-08-11 07:39:15

Contents:

.. code-block:: ts

    import { UmiPlugin } from '@metaplex-foundation/umi';
import { mplToolbox } from '@metaplex-foundation/mpl-toolbox';
import { createMplTokenMetadataProgram } from './generated';

export const mplTokenMetadata = (): UmiPlugin => ({
  install(umi) {
    umi.use(mplToolbox());
    umi.programs.add(createMplTokenMetadataProgram(), false);
  },
});


