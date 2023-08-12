packages/umi-rpc-web3js/src/plugin.ts
=====================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    import { UmiPlugin } from '@metaplex-foundation/umi';
import { createWeb3JsRpc, Web3JsRpcOptions } from './createWeb3JsRpc';

export const web3JsRpc = (
  endpoint: string,
  rpcOptions?: Web3JsRpcOptions
): UmiPlugin => ({
  install(umi) {
    umi.rpc = createWeb3JsRpc(umi, endpoint, rpcOptions);
  },
});


