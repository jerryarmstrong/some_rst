packages/core/react/src/errors.ts
=================================

Last edited: 2022-10-02 20:43:04

Contents:

.. code-block:: ts

    import { WalletError } from '@solana/wallet-adapter-base';

export class WalletNotSelectedError extends WalletError {
    name = 'WalletNotSelectedError';
}


