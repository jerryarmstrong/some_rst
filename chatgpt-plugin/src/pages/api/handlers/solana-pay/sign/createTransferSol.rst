chatgpt-plugin/src/pages/api/handlers/solana-pay/sign/createTransferSol.ts
==========================================================================

Last edited: 2023-08-04 21:04:21

Contents:

.. code-block:: ts

    import { NextApiRequest } from "next";
import { PublicKey, Transaction, SystemProgram, LAMPORTS_PER_SOL } from "@solana/web3.js";

import { makeRespondToSolanaPayGet, makeRespondToSolanaPayPost } from ".";
import configConstants, { CONNECTION } from "../../../constants";
configConstants();

async function createTransferSol(req: NextApiRequest) {
  const { destination, amount } = req.query;
  const { account: sender } = req.body;

  const tx = new Transaction();
  tx.add(
    SystemProgram.transfer({
      fromPubkey: new PublicKey(sender),
      toPubkey: new PublicKey(destination as string),
      lamports: Math.floor(parseFloat(amount as string) * LAMPORTS_PER_SOL),
    }),
  );
  tx.feePayer = new PublicKey(sender);
  tx.recentBlockhash = (await CONNECTION.getLatestBlockhash()).blockhash;

  return {
    transaction: tx.serialize({ requireAllSignatures: false }).toString("base64"),
  };
}

export default makeRespondToSolanaPayGet(makeRespondToSolanaPayPost(createTransferSol));


