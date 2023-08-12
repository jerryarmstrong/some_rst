packages/bridge/src/components/TokenDisplay/index.tsx
=====================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import { useConnectionConfig } from '@oyster/common';
import { TokenInfo } from '@solana/spl-token-registry';
import { debug } from 'console';
import React from 'react';
import { useEthereum } from '../../contexts';
import { ASSET_CHAIN } from '../../utils/assets';
import './style.less';
import { TokenChain } from './tokenChain';

export const TokenDisplay = ({
  asset,
  chain,
  token,
  logo,
}: {
  asset?: string;
  chain?: ASSET_CHAIN;
  token?: TokenInfo;
  logo?: string;
}) => {
  return (
    <div className="token-chain-logo">
      <img className="token-logo" alt="" src={logo || token?.logoURI} />
      {chain && <TokenChain chain={chain} className={'chain-logo'} />}
    </div>
  );
};


