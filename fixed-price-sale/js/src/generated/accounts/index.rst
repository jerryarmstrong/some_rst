fixed-price-sale/js/src/generated/accounts/index.ts
===================================================

Last edited: 2023-07-31 23:00:16

Contents:

.. code-block:: ts

    export * from './Market';
export * from './PayoutTicket';
export * from './PrimaryMetadataCreators';
export * from './SellingResource';
export * from './Store';
export * from './TradeHistory';

import { Store } from './Store';
import { SellingResource } from './SellingResource';
import { Market } from './Market';
import { TradeHistory } from './TradeHistory';
import { PrimaryMetadataCreators } from './PrimaryMetadataCreators';
import { PayoutTicket } from './PayoutTicket';

export const accountProviders = {
  Store,
  SellingResource,
  Market,
  TradeHistory,
  PrimaryMetadataCreators,
  PayoutTicket,
};


