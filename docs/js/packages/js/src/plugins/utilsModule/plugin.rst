packages/js/src/plugins/utilsModule/plugin.ts
=============================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import { UtilsClient } from './UtilsClient';
import type { Metaplex } from '@/Metaplex';
import { MetaplexPlugin } from '@/types';

/** @group Plugins */
export const utilsModule = (): MetaplexPlugin => ({
  install(metaplex: Metaplex) {
    const utilsClient = new UtilsClient(metaplex);
    metaplex.utils = () => utilsClient;
  },
});

declare module '../../Metaplex' {
  interface Metaplex {
    utils(): UtilsClient;
  }
}


