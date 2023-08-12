packages/rpc-core/src/rpc-methods/getBlocks.ts
==============================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { Commitment, Slot } from './common';

type GetBlocksApiResponse = Slot[];

export interface GetBlocksApi {
    /**
     * Returns a list of confirmed blocks between two slots
     */
    getBlocks(
        startSlot: Slot,
        endSlotInclusive?: Slot,
        config?: Readonly<{
            // Defaults to `finalized`
            commitment?: Exclude<Commitment, 'processed'>;
        }>
    ): GetBlocksApiResponse;
}


