packages/core/test/common.ts
============================

Last edited: 2023-01-05 08:54:11

Contents:

.. code-block:: ts

    import { PublicKey, Connection, LAMPORTS_PER_SOL } from '@solana/web3.js';

export async function airdropLamports(connection: Connection, ...to: PublicKey[]) {
    for (const publicKey of to) {
        const airdropSignature = await connection.requestAirdrop(publicKey, LAMPORTS_PER_SOL);
        await connection.confirmTransaction(airdropSignature);
    }
}

export async function sleep(ms: number) {
    return new Promise((resolve) => setTimeout(resolve, ms));
}


