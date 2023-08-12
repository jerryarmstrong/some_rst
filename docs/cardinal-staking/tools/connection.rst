tools/connection.ts
===================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { Connection } from "@solana/web3.js";
import * as dotenv from "dotenv";

dotenv.config();

const networkURLs: { [key: string]: string } = {
  ["mainnet-beta"]:
    process.env.MAINNET_PRIMARY_URL ?? "https://solana-api.projectserum.com",
  mainnet:
    process.env.MAINNET_PRIMARY_URL ?? "https://solana-api.projectserum.com",
  devnet: "https://api.devnet.solana.com/",
  testnet: "https://api.testnet.solana.com/",
  localnet: "http://localhost:8899/",
};

export const connectionFor = (cluster: string, defaultCluster = "mainnet") => {
  return new Connection(
    process.env.RPC_URL || networkURLs[cluster || defaultCluster] || "",
    "recent"
  );
};


