packages/server/src/connection.ts
=================================

Last edited: 2023-01-05 08:54:11

Contents:

.. code-block:: ts

    import { Connection } from '@solana/web3.js';
import config from '../../../config.json';

export const connection = new Connection(config.rpcUrl, 'confirmed');


