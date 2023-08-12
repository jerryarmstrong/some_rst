packages/js/src/plugins/bundlrStorage/plugin.ts
===============================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import { BundlrOptions, BundlrStorageDriver } from './BundlrStorageDriver';
import { Metaplex } from '@/Metaplex';
import { MetaplexPlugin } from '@/types';

export const bundlrStorage = (options: BundlrOptions = {}): MetaplexPlugin => ({
  install(metaplex: Metaplex) {
    metaplex.storage().setDriver(new BundlrStorageDriver(metaplex, options));
  },
});


