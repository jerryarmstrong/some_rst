src/utils/tradingview.tsx
=========================

Last edited: 2021-05-21 14:15:46

Contents:

.. code-block:: tsx

    import { USE_MARKETS } from './markets';

export const findTVMarketFromAddress = (marketAddressString: string) => {
  USE_MARKETS.forEach((market) => {
    if (market.address.toBase58() === marketAddressString) {
      return market.name;
    }
  });
  return 'SRM/USDC';
};


