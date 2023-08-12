packages/umi-rpc-chunk-get-accounts/src/createChunkGetAccountsRpc.ts
====================================================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    import { RpcInterface, chunk } from '@metaplex-foundation/umi';

export const createChunkGetAccountsRpc = (
  rpc: RpcInterface,
  chunkSize = 100
): RpcInterface => ({
  ...rpc,
  getAccounts: async (publicKeys, options) => {
    const promises = chunk(publicKeys, chunkSize).map((chunk) =>
      rpc.getAccounts(chunk, options)
    );
    const chunks = await Promise.all(promises);
    return chunks.flat();
  },
});


