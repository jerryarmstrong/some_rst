packages/wallets/ghost/src/initialize.ts
========================================

Last edited: 2023-08-07 05:28:02

Contents:

.. code-block:: ts

    import { registerWallet } from './register.js';
import { GhostWallet } from './wallet.js';
import type { Ghost } from './window.js';

export function initialize(ghost: Ghost): void {
    registerWallet(new GhostWallet(ghost));
}


