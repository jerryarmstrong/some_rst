packages/rpc-core/src/rpc-methods/getHealth.ts
==============================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    type GetHealthApiResponse = 'ok';

export interface GetHealthApi {
    /**
     * Returns the health status of the node ("ok" if healthy).
     */
    getHealth(
        // FIXME: https://github.com/solana-labs/solana-web3.js/issues/1389
        NO_CONFIG?: Record<string, never>
    ): GetHealthApiResponse;
}


