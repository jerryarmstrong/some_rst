examples/point-of-sale/src/client/hooks/useTransactions.ts
==========================================================

Last edited: 2023-05-03 15:27:33

Contents:

.. code-block:: ts

    import { TransactionConfirmationStatus, TransactionError, TransactionSignature } from '@solana/web3.js';
import { createContext, useContext } from 'react';
import { Confirmations } from '../types';

export interface Transaction {
    signature: TransactionSignature;
    amount: string;
    timestamp: number;
    error: TransactionError | null;
    status: TransactionConfirmationStatus;
    confirmations: Confirmations;
}

export interface TransactionsContextState {
    transactions: Transaction[];
    loading: boolean;
}

export const TransactionsContext = createContext<TransactionsContextState>({} as TransactionsContextState);

export function useTransactions(): TransactionsContextState {
    return useContext(TransactionsContext);
}


