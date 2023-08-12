chatgpt-plugin/src/pages/api/constants.ts
=========================================

Last edited: 2023-08-04 21:04:21

Contents:

.. code-block:: ts

    import express from "express";

import { Connection } from "@solana/web3.js";
import { HyperspaceClient } from "hyperspace-client-js";
import { RestClient } from "@hellomoon/api";

export const APP = express();
export const PORT = process.env.PORT || 3333;

import dotenv from "dotenv";
dotenv.config();

// Internal Solana Pay constants
export const SOLANA_PAY_LABEL = "Solana Labs ChatGPT Plugin";
export const TRANSACTION_ENDPOINTS = [
  "createBuyNFT",
  "createWriteNFTMetadata",
  "createCloseNFTMetadata",
];
export type TransactionEndpoints = (typeof TRANSACTION_ENDPOINTS)[number];
export const TX_DESCRIPTIONS: Record<TransactionEndpoints, string> = {
  createBuyNFT: "Sign to Buy NFT",
  createWriteNFTMetadata: "Sign to Write NFT Metadata",
  createCloseNFTMetadata: "Sign to Close NFT Metadata",
  createTransferToken: "Sign to Transfer Token",
  createTransferSol: "Sign to Transfer Sol",
};

// Inferred Constants
export let HELIUS_URL: string;
export let SELF_URL: string;
export let HYPERSPACE_CLIENT: HyperspaceClient;
export let HELLOMOON_CLIENT: RestClient;
export let CONNECTION: Connection;

export default function index() {
  HELIUS_URL = `https://rpc.helius.xyz/?api-key=${process.env.HELIUS_API_KEY}`;
  CONNECTION = new Connection(HELIUS_URL);

  if (process.env.DEV === "true") {
    SELF_URL = `http://localhost:${PORT}`;
  } else {
    SELF_URL = "https://chatgpt.solanalabs.com";
  }

  HYPERSPACE_CLIENT = new HyperspaceClient(process.env.HYPERSPACE_API_KEY as string);

  HELLOMOON_CLIENT = new RestClient(process.env.HELLOMOON_API_KEY as string);
}


