packages/umi-uploader-nft-storage/src/plugin.ts
===============================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    import type { UmiPlugin } from '@metaplex-foundation/umi';
import {
  createNftStorageUploader,
  NftStorageUploaderOptions,
} from './createNftStorageUploader';

export const nftStorageUploader = (
  options?: NftStorageUploaderOptions
): UmiPlugin => ({
  install(umi) {
    umi.uploader = createNftStorageUploader(umi, options);
  },
});


