src/constants.ts
================

Last edited: 2023-05-25 13:38:49

Contents:

.. code-block:: ts

    import { SuperCoder } from "@saberhq/anchor-contrib";
import { PublicKey } from "@solana/web3.js";

import type { MerkleDistributorTypes } from ".";
import { MerkleDistributorJSON } from "./idls/merkle_distributor";

export const PROGRAM_ID = new PublicKey(
  process.env.PROGRAM_ID || "DRoPZqPL5hjVsDyjokqKqMrW6DLzhGimjowQ9XSZHvrF"
);

export const MERKLE_DISTRIBUTOR_PROGRAM_ID = PROGRAM_ID;

export const MERKLE_DISTRIBUTOR_CODER = new SuperCoder<MerkleDistributorTypes>(
  MERKLE_DISTRIBUTOR_PROGRAM_ID,
  MerkleDistributorJSON
);


