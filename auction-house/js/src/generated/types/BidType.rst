auction-house/js/src/generated/types/BidType.ts
===============================================

Last edited: 2023-07-31 23:00:16

Contents:

.. code-block:: ts

    /**
 * This code was GENERATED using the solita package.
 * Please DO NOT EDIT THIS FILE, instead rerun solita to update it or write a wrapper to add functionality.
 *
 * See: https://github.com/metaplex-foundation/solita
 */

import * as beet from '@metaplex-foundation/beet';
/**
 * @category enums
 * @category generated
 */
export enum BidType {
  PublicSale,
  PrivateSale,
  AuctioneerPublicSale,
  AuctioneerPrivateSale,
}

/**
 * @category userTypes
 * @category generated
 */
export const bidTypeBeet = beet.fixedScalarEnum(BidType) as beet.FixedSizeBeet<BidType, BidType>;


