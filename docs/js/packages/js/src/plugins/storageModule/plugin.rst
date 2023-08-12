packages/js/src/plugins/storageModule/plugin.ts
===============================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import { StorageClient } from './StorageClient';
import type { Metaplex } from '@/Metaplex';
import { MetaplexPlugin } from '@/types';

/** @group Plugins */
export const storageModule = (): MetaplexPlugin => ({
  install(metaplex: Metaplex) {
    const storageClient = new StorageClient();
    metaplex.storage = () => storageClient;
  },
});

declare module '../../Metaplex' {
  interface Metaplex {
    storage(): StorageClient;
  }
}


