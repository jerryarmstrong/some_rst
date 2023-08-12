packages/rpc-core/src/rpc-methods/getMaxShredInsertSlot.ts
==========================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { Slot } from './common';

type GetMaxShredInsertSlotApiResponse = Slot;

export interface GetMaxShredInsertSlotApi {
    /**
     * Get the max slot seen from after shred insert.
     * Note that the optional NO_CONFIG object is ignored. See https://github.com/solana-labs/solana-web3.js/issues/1389
     */
    getMaxShredInsertSlot(
        // FIXME: https://github.com/solana-labs/solana-web3.js/issues/1389
        NO_CONFIG?: Record<string, never>
    ): GetMaxShredInsertSlotApiResponse;
}


