src/contexts/AutoConnectProvider.tsx
====================================

Last edited: 2023-06-24 05:42:55

Contents:

.. code-block:: tsx

    import { useLocalStorage } from '@solana/wallet-adapter-react';
import { createContext, FC, ReactNode, useContext } from 'react';

export interface AutoConnectContextState {
    autoConnect: boolean;
    setAutoConnect(autoConnect: boolean): void;
}

export const AutoConnectContext = createContext<AutoConnectContextState>({} as AutoConnectContextState);

export function useAutoConnect(): AutoConnectContextState {
    return useContext(AutoConnectContext);
}

export const AutoConnectProvider: FC<{ children: ReactNode }> = ({ children }) => {
    // TODO: fix auto connect to actual reconnect on refresh/other.
    // TODO: make switch/slider settings
    // const [autoConnect, setAutoConnect] = useLocalStorage('autoConnect', false);
    const [autoConnect, setAutoConnect] = useLocalStorage('autoConnect', true);

    return (
        <AutoConnectContext.Provider value={{ autoConnect, setAutoConnect }}>{children}</AutoConnectContext.Provider>
    );
};


