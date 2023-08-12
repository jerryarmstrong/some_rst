packages/metavinci/src/components/AppBar/index.tsx
==================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import React from 'react';
import './index.less';
import { Link, useLocation } from 'react-router-dom';
import { Button } from 'antd';
import { ConnectButton, CurrentUserBadge, useWallet } from '@oyster/common';

const UserActions = () => {
  return <>
    <Button className="app-btn">Bids</Button>
    <Link to={`/art/create`}>
      <Button className="app-btn">Create</Button>
    </Link>
    <Link to={`/auction/create/0`}>
      <Button type="primary">Sell</Button>
    </Link>
  </>;
}

export const AppBar = () => {
  const location = useLocation();
  const { connected } = useWallet();

  const isRoot = location.pathname === '/';


  return (
    <>
      <div className='app-left app-bar-box'>
        <h1 className="title">M</h1>
        <div className="divider" />
        <Link to={`/`}>
          <Button className="app-btn">Explore</Button>
        </Link>
        <Link to={`/user`}>
          <Button className="app-btn">Artworks</Button>
        </Link>
        <Link to={`/artists`}>
          <Button className="app-btn">Creators</Button>
        </Link>
      </div>
      {!connected && <ConnectButton type="primary" />}
      {connected && <div className='app-right app-bar-box'>
        <UserActions />
        <CurrentUserBadge showBalance={false} showAddress={false} iconSize={24}  />
      </div>}
    </>
  );
};


