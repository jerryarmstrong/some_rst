src/declarations.d.ts
=====================

Last edited: 2021-05-21 14:15:46

Contents:

.. code-block:: ts

    declare module '@project-serum/sol-wallet-adapter' {
  import EventEmitter from 'eventemitter3';
  import { PublicKey, Transaction } from '@solana/web3.js';

  export default class Wallet extends EventEmitter {
    constructor(providerUrl: string, network: string);
    publicKey: PublicKey;
    connected: boolean;
    autoApprove: boolean;
    connect: () => Promise<void>;
    disconnect: () => void;
    signTransaction: (transaction: Transaction) => Promise<Transaction>;
    signAllTransactions: (
      transactions: Transaction[],
    ) => Promise<Transaction[]>;
  }
}


