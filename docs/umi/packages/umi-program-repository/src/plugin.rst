packages/umi-program-repository/src/plugin.ts
=============================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    import { UmiPlugin } from '@metaplex-foundation/umi';
import { createDefaultProgramRepository } from './createDefaultProgramRepository';

export const defaultProgramRepository = (): UmiPlugin => ({
  install(umi) {
    umi.programs = createDefaultProgramRepository(umi);
  },
});


