clients/js-solita-candy-guard/src/generated/types/AllocationTracker.ts
======================================================================

Last edited: 2023-08-11 23:25:39

Contents:

.. code-block:: ts

    /**
 * This code was GENERATED using the solita package.
 * Please DO NOT EDIT THIS FILE, instead rerun solita to update it or write a wrapper to add functionality.
 *
 * See: https://github.com/metaplex-foundation/solita
 */

import * as beet from '@metaplex-foundation/beet';
export type AllocationTracker = {
  count: number;
};

/**
 * @category userTypes
 * @category generated
 */
export const allocationTrackerBeet = new beet.BeetArgsStruct<AllocationTracker>(
  [['count', beet.u32]],
  'AllocationTracker',
);


