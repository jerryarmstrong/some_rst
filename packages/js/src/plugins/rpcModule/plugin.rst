packages/js/src/plugins/rpcModule/plugin.ts
===========================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import { RpcClient } from './RpcClient';
import type { Metaplex } from '@/Metaplex';
import { MetaplexPlugin } from '@/types';

/** @group Plugins */
export const rpcModule = (): MetaplexPlugin => ({
  install(metaplex: Metaplex) {
    const rpcClient = new RpcClient(metaplex);
    metaplex.rpc = () => rpcClient;
  },
});

declare module '../../Metaplex' {
  interface Metaplex {
    rpc(): RpcClient;
  }
}


