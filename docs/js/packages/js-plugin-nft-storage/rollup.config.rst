packages/js-plugin-nft-storage/rollup.config.js
===============================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: js

    import { createConfigs } from '../../rollup.config';
import pkg from './package.json';

export default createConfigs({
  pkg,
  dependenciesToExcludeInBundle: [
    '@metaplex-foundation/js',
    '@ipld/dag-pb',
    '@nftstorage/metaplex-auth',
    'ipfs-car',
    'ipfs-unixfs',
    'multiformats',
    'nft.storage',
  ],
  builds: [
    {
      dir: 'dist/esm',
      format: 'es',
      bundle: true,
    },
    {
      dir: 'dist/cjs',
      format: 'cjs',
      bundle: true,
    },
  ],
});


