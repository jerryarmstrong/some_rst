packages/umi-transaction-factory-web3js/src/plugin.ts
=====================================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    import { UmiPlugin } from '@metaplex-foundation/umi';
import { createWeb3JsTransactionFactory } from './createWeb3JsTransactionFactory';

export const web3JsTransactionFactory = (): UmiPlugin => ({
  install(umi) {
    umi.transactions = createWeb3JsTransactionFactory();
  },
});


