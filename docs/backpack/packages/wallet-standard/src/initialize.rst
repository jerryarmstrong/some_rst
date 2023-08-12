packages/wallet-standard/src/initialize.ts
==========================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import type { ProviderSolanaInjection } from '@coral-xyz/provider-core';
import { DEPRECATED_registerWallet } from './register.js';
import { BackpackWallet } from './wallet.js';

export function initialize(backpack: ProviderSolanaInjection): void {
    DEPRECATED_registerWallet(new BackpackWallet(backpack));
}


