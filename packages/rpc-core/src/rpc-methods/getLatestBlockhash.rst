packages/rpc-core/src/rpc-methods/getLatestBlockhash.ts
=======================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { Blockhash } from '@solana/transactions';

import { Commitment, RpcResponse, Slot, U64UnsafeBeyond2Pow53Minus1 } from './common';

type GetLatestBlockhashApiResponse = RpcResponse<{
    /** a Hash as base-58 encoded string */
    blockhash: Blockhash;
    /** last block height at which the blockhash will be valid */
    lastValidBlockHeight: U64UnsafeBeyond2Pow53Minus1;
}>;

export interface GetLatestBlockhashApi {
    /**
     * Returns the latest blockhash
     */
    getLatestBlockhash(
        config?: Readonly<{
            commitment?: Commitment;
            minContextSlot?: Slot;
        }>
    ): GetLatestBlockhashApiResponse;
}


