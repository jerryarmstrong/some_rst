packages/core/features/src/index.ts
===================================

Last edited: 2023-08-07 05:28:02

Contents:

.. code-block:: ts

    import type { WalletWithFeatures } from '@wallet-standard/base';
import type { SolanaSignAndSendTransactionFeature } from './signAndSendTransaction.js';
import type { SolanaSignInFeature } from './signIn.js';
import type { SolanaSignMessageFeature } from './signMessage.js';
import type { SolanaSignTransactionFeature } from './signTransaction.js';

/** TODO: docs */
export type SolanaFeatures =
    | SolanaSignAndSendTransactionFeature
    | SolanaSignInFeature
    | SolanaSignMessageFeature
    | SolanaSignTransactionFeature;

/** TODO: docs */
export type WalletWithSolanaFeatures = WalletWithFeatures<SolanaFeatures>;

export * from './signAndSendTransaction.js';
export * from './signIn.js';
export * from './signMessage.js';
export * from './signTransaction.js';


