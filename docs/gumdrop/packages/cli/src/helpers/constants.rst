packages/cli/src/helpers/constants.ts
=====================================

Last edited: 2022-08-25 19:21:42

Contents:

.. code-block:: ts

    import { PublicKey } from '@solana/web3.js';

export const CANDY_MACHINE_PROGRAM_V2_ID = new PublicKey(
  'cndy3Z4yapfJBmL3ShUp5exZKqR3z33thTzeNMm2gRZ',
);
export const TOKEN_METADATA_PROGRAM_ID = new PublicKey(
  'metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s',
);
export const SPL_ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID = new PublicKey(
  'ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL',
);
export const TOKEN_PROGRAM_ID = new PublicKey(
  'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA',
);
export const GUMDROP_DISTRIBUTOR_ID = new PublicKey(
  'gdrpGjVffourzkdDRrQmySw4aTHr8a3xmQzzxSwFD1a',
);
export const GUMDROP_TEMPORAL_SIGNER = new PublicKey(
  'MSv9H2sMceAzccBganUXwGq3GXgqYAstmZAbFDZYbAV',
);

export const DEFAULT_TIMEOUT = 15000;


