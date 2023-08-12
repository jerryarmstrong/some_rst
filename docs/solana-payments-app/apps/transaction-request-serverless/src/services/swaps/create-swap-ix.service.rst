apps/transaction-request-serverless/src/services/swaps/create-swap-ix.service.ts
================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import * as web3 from '@solana/web3.js';
import { createJupiterSwapIx } from './jupiter.service.js';

export type SwapProvider = 'jupiter';

export interface SwapIxConfig {
    provider: SwapProvider;
    quantity: number;
    swapingWallet: web3.PublicKey;
    fromMint: web3.PublicKey;
    toMint: web3.PublicKey;
}

export const createSwapIx = async (config: SwapIxConfig): Promise<web3.TransactionInstruction[]> => {
    switch (config.provider) {
        case 'jupiter':
            return createJupiterSwapIx(config);
    }
};


