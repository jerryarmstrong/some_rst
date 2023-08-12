packages/common/src/solana/transaction-helpers.ts
=================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import { Transaction, VersionedTransaction } from "@solana/web3.js";
import { ethers } from "ethers";
const { base58: bs58 } = ethers.utils;

export const deserializeTransaction = (serializedTx: string) => {
  return VersionedTransaction.deserialize(bs58.decode(serializedTx));
};

export const deserializeLegacyTransaction = (serializedTx: string) => {
  return Transaction.from(bs58.decode(serializedTx));
};

export const isVersionedTransaction = (
  tx: Transaction | VersionedTransaction
): tx is VersionedTransaction => {
  return "version" in tx;
};


