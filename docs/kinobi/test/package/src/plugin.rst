test/package/src/plugin.ts
==========================

Last edited: 2023-08-04 12:58:33

Contents:

.. code-block:: ts

    import type { Umi, UmiPlugin } from '@metaplex-foundation/umi';
import {
  createMplCandyMachineCoreProgram,
  createMplTokenAuthRulesProgram,
  createMplTokenMetadataProgram,
} from './generated';

export function plugin(): UmiPlugin {
  return {
    install(umi: Umi) {
      umi.programs.add(createMplCandyMachineCoreProgram(), false);
      umi.programs.add(createMplTokenAuthRulesProgram(), false);
      umi.programs.add(createMplTokenMetadataProgram(), false);
    },
  };
}


