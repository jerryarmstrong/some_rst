js/packages/web/src/components/AuctionCard/hooks/useActionButtonContent.ts
==========================================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import { AuctionView } from '../../../hooks';
import { useInstantSaleState } from './useInstantSaleState';

export const useActionButtonContent = (auctionView: AuctionView): string => {
  const {
    isInstantSale,
    canClaimItem,
    canClaimPurchasedItem,
    canEndInstantSale,
  } = useInstantSaleState(auctionView);

  if (!isInstantSale) {
    return 'Place Bid';
  }

  if (canClaimPurchasedItem) {
    return 'Claim Purchase';
  }

  if (canClaimItem) {
    return 'Claim item';
  }

  if (canEndInstantSale) {
    return 'End sale & claim item';
  }

  return 'Buy now';
};


