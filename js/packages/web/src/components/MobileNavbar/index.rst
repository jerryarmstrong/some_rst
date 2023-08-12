js/packages/web/src/components/MobileNavbar/index.tsx
=====================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: tsx

    import React from 'react';
import { useWallet } from '@solana/wallet-adapter-react';

import { Notifications } from '../Notifications';
import { LogoLink, MetaplexMenu } from '../AppBar';

export const MobileNavbar = () => {
  const { connected } = useWallet();

  return (
    <div id="mobile-navbar">
      <LogoLink />
      <div className="mobile-menu">
        {connected && <Notifications />}
        <MetaplexMenu />
      </div>
    </div>
  );
};


