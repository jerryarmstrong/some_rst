packages/common/src/tokens/types.ts
===================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    export type TokenListEntry = {
  __typename?: "TokenListEntry";
  /** The mint or contract address of the token. */
  address: string;
  /** The Coingecko market listing ID. */
  coingeckoId?: string;
  /** The logo associated with the token. */
  logo?: string;
  /** The registered name of the token. */
  name: string;
  /** The registered symbol of the token. */
  symbol: string;
};

export type CustomTokenList = {
  native: TokenListEntry;
  [addr: string]: TokenListEntry;
};


