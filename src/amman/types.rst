src/amman/types.ts
==================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: ts

    import { TransactionSignature } from "@solana/web3.js";

export type TransactionSignatureWithBlock = {
  block: number;
  signature: TransactionSignature;
};


