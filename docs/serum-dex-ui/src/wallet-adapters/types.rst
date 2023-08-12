src/wallet-adapters/types.ts
============================

Last edited: 2021-05-21 14:15:46

Contents:

.. code-block:: ts

    import { PublicKey, Transaction } from '@solana/web3.js';

export const DEFAULT_PUBLIC_KEY = new PublicKey(
  '11111111111111111111111111111111',
);

export interface WalletAdapter {
  publicKey: PublicKey;
  autoApprove: boolean;
  connected: boolean;
  signTransaction: (transaction: Transaction) => Promise<Transaction>;
  signAllTransactions: (transaction: Transaction[]) => Promise<Transaction[]>;
  connect: () => any;
  disconnect: () => any;
  on<T>(event: string, fn: () => void): this;
}


