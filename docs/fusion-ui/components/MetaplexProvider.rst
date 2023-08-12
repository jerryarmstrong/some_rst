components/MetaplexProvider.tsx
===============================

Last edited: 2023-02-28 18:04:35

Contents:

.. code-block:: tsx

    import { Provider, useMemo, FC } from 'react';
import { useWallet, useConnection } from '@solana/wallet-adapter-react';
import { Metaplex, walletAdapterIdentity } from "@metaplex-foundation/js";
import { MetaplexContext } from '../hooks/useMetaplex';

interface MetaplexProviderProps { children: React.ReactNode }

export const MetaplexProvider: FC<MetaplexProviderProps> = ({ children }) => {
    const { connection } = useConnection();
    const wallet = useWallet();

    const metaplex = useMemo(() => {
        if (!wallet) {
            console.error("wallet not connected");
            return null;
        }
        return Metaplex.make(connection).use(
            walletAdapterIdentity(wallet),
        );
    }, [connection, wallet]);

    return (
        <MetaplexContext.Provider value={{ metaplex }}>
            {children}
        </MetaplexContext.Provider>
    );
};

