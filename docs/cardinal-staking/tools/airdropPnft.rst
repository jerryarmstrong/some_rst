tools/airdropPnft.ts
====================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { utils, Wallet } from "@coral-xyz/anchor";
import { Keypair } from "@solana/web3.js";

import { createProgrammableAsset } from "../tests/utils";
import { connectionFor } from "./connection";

const wallet = new Wallet(
  Keypair.fromSecretKey(utils.bytes.bs58.decode(process.env.WALLET || ""))
);

const main = async (cluster = "devnet") => {
  const connection = connectionFor(cluster);
  const [, , , txid] = await createProgrammableAsset(
    connection,
    wallet,
    "https://arweave.net/tbzsgNCBxiBi9Cemxln1CtDlL8_Knq1tXJLOrIuYHb8"
  );
  console.log(
    "txid",
    `https://explorer.solana.com/tx/${txid}?cluster=${cluster}`
  );
};

main().catch((e) => console.log(e));


