packages/core/react/src/useConnection.tsx
=========================================

Last edited: 2022-10-02 20:43:04

Contents:

.. code-block:: tsx

    import type { Connection } from '@solana/web3.js';
import { createContext, useContext } from 'react';

export interface ConnectionContextState {
    connection: Connection;
}

export const ConnectionContext = createContext<ConnectionContextState>({} as ConnectionContextState);

export function useConnection(): ConnectionContextState {
    return useContext(ConnectionContext);
}


