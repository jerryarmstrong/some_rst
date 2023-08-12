packages/rpc-core/src/rpc-methods/getBlockTime.ts
=================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { UnixTimestamp } from '../unix-timestamp';
import { Slot } from './common';

/** Estimated production time, as Unix timestamp (seconds since the Unix epoch) */
type GetBlockTimeApiResponse = UnixTimestamp;

export interface GetBlockTimeApi {
    /**
     * Returns the estimated production time of a block.
     */
    getBlockTime(
        /** block number, identified by Slot */
        blockNumber: Slot
    ): GetBlockTimeApiResponse;
}


