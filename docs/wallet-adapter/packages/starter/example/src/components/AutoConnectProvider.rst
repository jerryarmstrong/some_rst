packages/starter/example/src/components/AutoConnectProvider.tsx
===============================================================

Last edited: 2022-10-02 20:43:04

Contents:

.. code-block:: tsx

    import { useLocalStorage } from '@solana/wallet-adapter-react';
import type { FC, ReactNode } from 'react';
import React, { createContext, useContext } from 'react';

export interface AutoConnectContextState {
    autoConnect: boolean;
    setAutoConnect(autoConnect: boolean): void;
}

export const AutoConnectContext = createContext<AutoConnectContextState>({} as AutoConnectContextState);

export function useAutoConnect(): AutoConnectContextState {
    return useContext(AutoConnectContext);
}

export const AutoConnectProvider: FC<{ children: ReactNode }> = ({ children }) => {
    const [autoConnect, setAutoConnect] = useLocalStorage('autoConnect', false);

    return (
        <AutoConnectContext.Provider value={{ autoConnect, setAutoConnect }}>{children}</AutoConnectContext.Provider>
    );
};


