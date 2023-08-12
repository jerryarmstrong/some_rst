packages/core/react/src/ConnectionProvider.tsx
==============================================

Last edited: 2022-10-02 20:43:04

Contents:

.. code-block:: tsx

    import type { ConnectionConfig } from '@solana/web3.js';
import { Connection } from '@solana/web3.js';
import type { FC, ReactNode } from 'react';
import React, { useMemo } from 'react';
import { ConnectionContext } from './useConnection.js';

export interface ConnectionProviderProps {
    children: ReactNode;
    endpoint: string;
    config?: ConnectionConfig;
}

export const ConnectionProvider: FC<ConnectionProviderProps> = ({
    children,
    endpoint,
    config = { commitment: 'confirmed' },
}) => {
    const connection = useMemo(() => new Connection(endpoint, config), [endpoint, config]);

    return <ConnectionContext.Provider value={{ connection }}>{children}</ConnectionContext.Provider>;
};


