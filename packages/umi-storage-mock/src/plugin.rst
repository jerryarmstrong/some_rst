packages/umi-storage-mock/src/plugin.ts
=======================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    import { UmiPlugin } from '@metaplex-foundation/umi';
import { createMockStorage, MockStorageOptions } from './createMockStorage';

export const mockStorage = (options?: MockStorageOptions): UmiPlugin => ({
  install(umi) {
    const mockStorage = createMockStorage(options);
    umi.uploader = mockStorage;
    umi.downloader = mockStorage;
  },
});


