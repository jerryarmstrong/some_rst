packages/core/base/src/types.ts
===============================

Last edited: 2023-08-07 04:48:35

Contents:

.. code-block:: ts

    import type { WalletAdapter } from './adapter.js';
import type { MessageSignerWalletAdapter, SignerWalletAdapter, SignInMessageSignerWalletAdapter } from './signer.js';
import type { StandardWalletAdapter } from './standard.js';

export type Adapter =
    | WalletAdapter
    | SignerWalletAdapter
    | MessageSignerWalletAdapter
    | SignInMessageSignerWalletAdapter
    | StandardWalletAdapter;

export enum WalletAdapterNetwork {
    Mainnet = 'mainnet-beta',
    Testnet = 'testnet',
    Devnet = 'devnet',
}


