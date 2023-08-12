clients/js/src/plugin.ts
========================

Last edited: 2023-07-16 23:08:25

Contents:

.. code-block:: ts

    import { UmiPlugin } from '@metaplex-foundation/umi';
import { createMplProjectNameProgram } from './generated';

export const mplProjectName = (): UmiPlugin => ({
  install(umi) {
    umi.programs.add(createMplProjectNameProgram(), false);
  },
});


