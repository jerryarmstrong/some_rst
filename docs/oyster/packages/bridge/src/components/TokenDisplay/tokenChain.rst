packages/bridge/src/components/TokenDisplay/tokenChain.tsx
==========================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import React from 'react';
import { ASSET_CHAIN } from '../../utils/assets';

export const TokenChain = (props: {
  chain?: ASSET_CHAIN;
  className?: string;
}) => {
  const { chain, className } = props;
  return (
    <img
      className={`chain-logo ${className}`}
      alt=""
      src={
        chain === ASSET_CHAIN.Ethereum
          ? '/blockchains/ETH.svg'
          : '/blockchains/solana.webp'
      }
    />
  );
};


