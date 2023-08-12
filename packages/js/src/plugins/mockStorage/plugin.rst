packages/js/src/plugins/mockStorage/plugin.ts
=============================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import { MockStorageDriver, MockStorageOptions } from './MockStorageDriver';
import { Metaplex } from '@/Metaplex';
import { MetaplexPlugin } from '@/types';

export const mockStorage = (options?: MockStorageOptions): MetaplexPlugin => ({
  install(metaplex: Metaplex) {
    metaplex.storage().setDriver(new MockStorageDriver(options));
  },
});


