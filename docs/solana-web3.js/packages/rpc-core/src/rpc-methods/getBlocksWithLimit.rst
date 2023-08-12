packages/rpc-core/src/rpc-methods/getBlocksWithLimit.ts
=======================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { Commitment, Slot } from './common';

type GetBlocksWithLimitApiResponse = Slot[];

export interface GetBlocksWithLimitApi {
    /**
     * Returns a list of confirmed blocks starting at the given slot
     * for up to `limit` blocks
     */
    getBlocksWithLimit(
        startSlot: Slot,
        // The maximum number of blocks to return (between 0 and 500,000)
        // Note: 0 will return an empty array
        limit: number,
        config?: Readonly<{
            // Defaults to `finalized`
            commitment?: Exclude<Commitment, 'processed'>;
        }>
    ): GetBlocksWithLimitApiResponse;
}


