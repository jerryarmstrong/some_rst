src/pages/api/createTrifleAccountTx.ts
======================================

Last edited: 2023-03-12 23:06:11

Contents:

.. code-block:: ts

    // Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from 'next'
import { Connection, Keypair, PublicKey, Signer, TransactionInstruction, TransactionMessage, Version, VersionedTransaction } from '@solana/web3.js';

type Data = {
    tx: any,
}

function loadEnvKey(): Keypair {
    const loaded = Keypair.fromSecretKey(
        new Uint8Array(JSON.parse(process.env.FUSION_AUTH_KEYPAIR)),
    );
    console.log(`wallet public key: ${loaded.publicKey}`);
    return loaded;
}

export default async function handler(
    req: NextApiRequest,
    res: NextApiResponse<Data>
) {
    const transaction = VersionedTransaction.deserialize(Uint8Array.from(Buffer.from(req.body, "base64")));
    // const payerKey = req.body as PublicKey;
    const authKey = loadEnvKey();
    // const connection = new Connection(process.env.RPC_ENDPOINT_MAINNET);
    // const instructions: TransactionInstruction[] = [];

    // let blockhash = await connection
    //     .getLatestBlockhash()
    //     .then((res) => res.blockhash);

    // // create v0 compatible message
    // const messageV0 = new TransactionMessage({
    //     payerKey,
    //     recentBlockhash: blockhash,
    //     instructions,
    // }).compileToV0Message();

    // const transaction = new VersionedTransaction(messageV0);

    // // sign your transaction with the required `Signers`
    transaction.sign([authKey]);

    res.status(200).json({ tx: Buffer.from(transaction.serialize()).toString("base64") })
}


