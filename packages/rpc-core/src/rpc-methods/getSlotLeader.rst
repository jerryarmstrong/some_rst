packages/rpc-core/src/rpc-methods/getSlotLeader.ts
==================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { Base58EncodedAddress } from '@solana/addresses';

import { Commitment, Slot } from './common';

export interface GetSlotLeaderApi {
    /**
     * Returns the current slot leader
     */
    getSlotLeader(
        config?: Readonly<{
            commitment?: Commitment;
            minContextSlot?: Slot;
        }>
    ): Base58EncodedAddress;
}


