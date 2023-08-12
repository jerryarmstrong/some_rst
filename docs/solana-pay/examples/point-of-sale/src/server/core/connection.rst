examples/point-of-sale/src/server/core/connection.ts
====================================================

Last edited: 2023-05-03 15:27:33

Contents:

.. code-block:: ts

    import { Connection } from '@solana/web3.js';
import { CLUSTER_ENDPOINT } from './env';

export const connection = new Connection(CLUSTER_ENDPOINT, 'confirmed');


