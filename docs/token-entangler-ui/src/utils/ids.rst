src/utils/ids.ts
================

Last edited: 2022-06-29 05:55:18

Contents:

.. code-block:: ts

    import { PublicKey } from "@solana/web3.js";

export type StringPublicKey = string;

export const CANDY_MACHINE_ID = new PublicKey(
  "cndyAnrLdpjq1Ssp1z8xxDsB8dxe7u4HL5Nxi2K5WXZ"
);

export const GUMDROP_DISTRIBUTOR_ID = new PublicKey(
  "gdrpGjVffourzkdDRrQmySw4aTHr8a3xmQzzxSwFD1a"
);

export const GUMDROP_TEMPORAL_SIGNER = new PublicKey(
  "MSv9H2sMceAzccBganUXwGq3GXgqYAstmZAbFDZYbAV"
);

export const SPL_ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID = new PublicKey(
  "ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL"
);

export const TOKEN_METADATA_PROGRAM_ID = new PublicKey(
  "metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s"
);

export const TOKEN_ENTANGLEMENT_PROGRAM_ID = new PublicKey(
  "qntmGodpGkrM42mN68VCZHXnKqDCT8rdY23wFcXCLPd"
);

export const WRAPPED_SOL_MINT = new PublicKey(
  "So11111111111111111111111111111111111111112"
);


