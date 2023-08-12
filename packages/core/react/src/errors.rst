packages/core/react/src/errors.ts
=================================

Last edited: 2023-08-07 04:48:35

Contents:

.. code-block:: ts

    import { WalletError } from '@solana/wallet-adapter-base';

export class WalletNotSelectedError extends WalletError {
    name = 'WalletNotSelectedError';
}


