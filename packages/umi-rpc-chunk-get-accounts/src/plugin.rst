packages/umi-rpc-chunk-get-accounts/src/plugin.ts
=================================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    import { UmiPlugin } from '@metaplex-foundation/umi';
import { createChunkGetAccountsRpc } from './createChunkGetAccountsRpc';

export const chunkGetAccountsRpc = (chunkSize = 100): UmiPlugin => ({
  install(umi) {
    umi.rpc = createChunkGetAccountsRpc(umi.rpc, chunkSize);
  },
});


