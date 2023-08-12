packages/rpc-core/src/rpc-methods/minimumLedgerSlot.ts
======================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { Slot } from './common';

type MinimumLedgerSlotApiResponse = Slot;

export interface MinimumLedgerSlotApi {
    /**
     * Returns the lowest slot that the node has information about in its ledger.
     * This value may increase over time if the node is configured to purge older ledger data.
     */
    minimumLedgerSlot(): MinimumLedgerSlotApiResponse;
}


