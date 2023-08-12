core/example/payment-flow-merchant/establishConnection.ts
=========================================================

Last edited: 2023-05-03 15:27:33

Contents:

.. code-block:: ts

    import type { Cluster } from '@solana/web3.js';
import { clusterApiUrl, Connection } from '@solana/web3.js';

/**
 * Establish a connection to the cluster
 */
export async function establishConnection(cluster: Cluster = 'devnet'): Promise<Connection> {
    const endpoint = clusterApiUrl(cluster);
    const connection = new Connection(endpoint, 'confirmed');
    const version = await connection.getVersion();
    console.log('Connection to cluster established:', endpoint, version);

    return connection;
}


