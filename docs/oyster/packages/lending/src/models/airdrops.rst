packages/lending/src/models/airdrops.ts
=======================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { PublicKey } from '@solana/web3.js';

interface PoolAirdrop {
  pool: PublicKey;
  airdrops: {
    mint: PublicKey;
    amount: number;
  }[];
}

export const POOLS_WITH_AIRDROP: PoolAirdrop[] = [];


