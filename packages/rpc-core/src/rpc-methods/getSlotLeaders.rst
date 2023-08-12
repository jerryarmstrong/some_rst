packages/rpc-core/src/rpc-methods/getSlotLeaders.ts
===================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { Base58EncodedAddress } from '@solana/addresses';

import { Slot } from './common';

/** array of Node identity public keys as base-58 encoded strings */
type GetSlotLeadersApiResponse = Base58EncodedAddress[];

export interface GetSlotLeadersApi {
    /**
     * Returns the slot leaders for a given slot range
     */
    getSlotLeaders(
        /** Start slot, as u64 integer */
        startSlot: Slot,
        /** Limit (between 1 and 5000) */
        limit: number
    ): GetSlotLeadersApiResponse;
}


