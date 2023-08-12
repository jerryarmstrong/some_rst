packages/rpc-core/src/rpc-methods/getVersion.ts
===============================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    type GetVersionApiResponse = Readonly<{
    /** Unique identifier of the current software's feature set */
    'feature-set': number;
    /** Software version of `solana-core` */
    'solana-core': string;
}>;

export interface GetVersionApi {
    /**
     * Returns the current Solana version running on the node
     */
    getVersion(
        // FIXME: https://github.com/solana-labs/solana-web3.js/issues/1389
        NO_CONFIG?: Record<string, never>
    ): GetVersionApiResponse;
}


