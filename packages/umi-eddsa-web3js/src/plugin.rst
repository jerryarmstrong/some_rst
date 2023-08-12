packages/umi-eddsa-web3js/src/plugin.ts
=======================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    import { UmiPlugin } from '@metaplex-foundation/umi';
import { createWeb3JsEddsa } from './createWeb3JsEddsa';

export const web3JsEddsa = (): UmiPlugin => ({
  install(umi) {
    umi.eddsa = createWeb3JsEddsa();
  },
});


