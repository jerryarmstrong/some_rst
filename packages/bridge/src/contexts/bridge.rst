packages/bridge/src/contexts/bridge.tsx
=======================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import React, { createContext, FunctionComponent, useContext } from 'react';
import { SolanaBridge } from '@solana/bridge-sdk';
import {
  useConnection,
  useConnectionConfig,
} from '@oyster/common/dist/lib/contexts/connection';
import { utils } from '@oyster/common';

export const BridgeContext = createContext<SolanaBridge | undefined>(undefined);

export const BridgeProvider: FunctionComponent = ({ children }) => {
  const { endpoint } = useConnectionConfig();
  const connection = useConnection();
  const programs = utils.programIds();

  let bridge = new SolanaBridge(
    endpoint,
    connection,
    programs.wormhole.pubkey,
    programs.token,
  );

  return (
    <BridgeContext.Provider value={bridge}>{children}</BridgeContext.Provider>
  );
};

export const useBridge = () => {
  const bridge = useContext(BridgeContext);
  return bridge;
};


