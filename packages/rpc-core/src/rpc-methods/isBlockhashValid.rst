packages/rpc-core/src/rpc-methods/isBlockhashValid.ts
=====================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { Blockhash } from '@solana/transactions';

import { Commitment, RpcResponse, Slot } from './common';

type IsBlockhashValidApiResponse = RpcResponse<boolean>;

export interface IsBlockhashValidApi {
    /**
     * Returns whether a blockhash is still valid or not
     */
    isBlockhashValid(
        /** query blockhash, as a base-58 encoded string */
        blockhash: Blockhash,
        config?: Readonly<{
            /** Defaults to `finalized` */
            commitment?: Commitment;
            /** The minimum slot that the request can be evaluated at */
            minContextSlot?: Slot;
        }>
    ): IsBlockhashValidApiResponse;
}


