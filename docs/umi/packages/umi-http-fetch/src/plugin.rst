packages/umi-http-fetch/src/plugin.ts
=====================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    import { UmiPlugin } from '@metaplex-foundation/umi';
import { createFetchHttp } from './createFetchHttp';

export const fetchHttp = (): UmiPlugin => ({
  install(umi) {
    umi.http = createFetchHttp();
  },
});


