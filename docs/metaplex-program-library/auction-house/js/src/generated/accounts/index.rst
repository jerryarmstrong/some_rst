auction-house/js/src/generated/accounts/index.ts
================================================

Last edited: 2023-07-31 23:00:16

Contents:

.. code-block:: ts

    export * from './AuctionHouse';
export * from './Auctioneer';
export * from './BidReceipt';
export * from './ListingReceipt';
export * from './PurchaseReceipt';

import { BidReceipt } from './BidReceipt';
import { ListingReceipt } from './ListingReceipt';
import { PurchaseReceipt } from './PurchaseReceipt';
import { AuctionHouse } from './AuctionHouse';
import { Auctioneer } from './Auctioneer';

export const accountProviders = {
  BidReceipt,
  ListingReceipt,
  PurchaseReceipt,
  AuctionHouse,
  Auctioneer,
};


