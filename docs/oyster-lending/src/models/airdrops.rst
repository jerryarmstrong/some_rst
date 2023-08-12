src/models/airdrops.ts
======================

Last edited: 2021-03-16 20:45:52

Contents:

.. code-block:: ts

    import { PublicKey } from "@solana/web3.js";

interface PoolAirdrop {
  pool: PublicKey;
  airdrops: {
    mint: PublicKey;
    amount: number;
  }[];
}

export const POOLS_WITH_AIRDROP: PoolAirdrop[] = [];


