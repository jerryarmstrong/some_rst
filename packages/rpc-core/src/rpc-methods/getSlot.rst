packages/rpc-core/src/rpc-methods/getSlot.ts
============================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { Commitment, Slot } from './common';

type GetSlotApiResponse = Slot;

export interface GetSlotApi {
    /**
     * Returns the slot that has reached the given or default commitment level
     */
    getSlot(
        config?: Readonly<{
            commitment?: Commitment;
            minContextSlot?: Slot;
        }>
    ): GetSlotApiResponse;
}


