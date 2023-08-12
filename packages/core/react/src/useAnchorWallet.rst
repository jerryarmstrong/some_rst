packages/core/react/src/useAnchorWallet.ts
==========================================

Last edited: 2023-08-07 04:48:35

Contents:

.. code-block:: ts

    import { type PublicKey, type Transaction, type VersionedTransaction } from '@solana/web3.js';
import { useMemo } from 'react';
import { useWallet } from './useWallet.js';

export interface AnchorWallet {
    publicKey: PublicKey;
    signTransaction<T extends Transaction | VersionedTransaction>(transaction: T): Promise<T>;
    signAllTransactions<T extends Transaction | VersionedTransaction>(transactions: T[]): Promise<T[]>;
}

export function useAnchorWallet(): AnchorWallet | undefined {
    const { publicKey, signTransaction, signAllTransactions } = useWallet();
    return useMemo(
        () =>
            publicKey && signTransaction && signAllTransactions
                ? { publicKey, signTransaction, signAllTransactions }
                : undefined,
        [publicKey, signTransaction, signAllTransactions]
    );
}


