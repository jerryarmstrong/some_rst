js/packages/common/src/contexts/meta/getEmptyMetaState.ts
=========================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import { MetaState } from './types';

export const getEmptyMetaState = (): MetaState => ({
  metadata: [],
  metadataByMetadata: {},
  metadataByMint: {},
  metadataByCollection: {},
  metadataByAuction: {},
  masterEditions: {},
  masterEditionsByPrintingMint: {},
  masterEditionsByOneTimeAuthMint: {},
  metadataByMasterEdition: {},
  editions: {},
  auctionManagersByAuction: {},
  bidRedemptions: {},
  auctions: {},
  auctionDataExtended: {},
  vaults: {},
  payoutTickets: {},
  store: null,
  whitelistedCreatorsByCreator: {},
  bidderMetadataByAuctionAndBidder: {},
  bidderPotsByAuctionAndBidder: {},
  safetyDepositBoxesByVaultAndIndex: {},
  prizeTrackingTickets: {},
  safetyDepositConfigsByAuctionManagerAndIndex: {},
  bidRedemptionV2sByAuctionManagerAndWinningIndex: {},
  auctionCaches: {},
  storeIndexer: [],
  packs: {},
  packCards: {},
  packCardsByPackSet: {},
  vouchers: {},
  provingProcesses: {},
});


