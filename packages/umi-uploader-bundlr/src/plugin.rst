packages/umi-uploader-bundlr/src/plugin.ts
==========================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    import type { UmiPlugin } from '@metaplex-foundation/umi';
import {
  BundlrUploaderOptions,
  createBundlrUploader,
} from './createBundlrUploader';

export const bundlrUploader = (options?: BundlrUploaderOptions): UmiPlugin => ({
  install(umi) {
    umi.uploader = createBundlrUploader(umi, options);
  },
});


