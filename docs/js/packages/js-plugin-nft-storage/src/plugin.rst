packages/js-plugin-nft-storage/src/plugin.ts
============================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import type { Metaplex, MetaplexPlugin } from '@metaplex-foundation/js';
import { NftStorageDriver, NftStorageDriverOptions } from './NftStorageDriver';

export const nftStorage = (
  options: NftStorageDriverOptions = {}
): MetaplexPlugin => ({
  install(metaplex: Metaplex) {
    metaplex.storage().setDriver(new NftStorageDriver(metaplex, options));
  },
});


