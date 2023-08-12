packages/rpc-core/src/rpc-methods/getTransactionCount.ts
========================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { Commitment, Slot, U64UnsafeBeyond2Pow53Minus1 } from './common';

type GetTransactionCountApiResponse = U64UnsafeBeyond2Pow53Minus1;

export interface GetTransactionCountApi {
    /**
     * Returns the current Transaction count from the ledger
     */
    getTransactionCount(
        config?: Readonly<{
            // Defaults to `finalized`
            commitment?: Commitment;
            // The minimum slot that the request can be evaluated at
            minContextSlot?: Slot;
        }>
    ): GetTransactionCountApiResponse;
}


