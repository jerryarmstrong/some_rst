packages/bridge/src/components/CurrentUserWalletBadge/index.tsx
===============================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import React from 'react';

import { shortenAddress, useWallet } from '@oyster/common';

export const CurrentUserWalletBadge = (props: { showDisconnect?: boolean }) => {
  const { wallet, publicKey, disconnect } = useWallet();

  if (!wallet || !publicKey) {
    return null;
  }

  return (
    <div className="wallet-wrapper">
      <div className="wallet-key">
        <img
          alt={'icon'}
          width={20}
          height={20}
          src={wallet.icon}
          style={{ marginRight: 8 }}
        />
        {shortenAddress(`${publicKey}`)}
        {props.showDisconnect && (
          <span className={'disconnect'} onClick={() => disconnect()}>
            X
          </span>
        )}
      </div>
    </div>
  );
};


