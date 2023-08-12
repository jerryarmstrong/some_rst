clients/js/src/plugin.ts
========================

Last edited: 2023-08-01 17:12:05

Contents:

.. code-block:: ts

    import { UmiPlugin } from '@metaplex-foundation/umi';
import { createMplTokenAuthRulesProgram } from './generated';

export const mplTokenAuthRules = (): UmiPlugin => ({
  install(umi) {
    umi.programs.add(createMplTokenAuthRulesProgram(), false);
  },
});


