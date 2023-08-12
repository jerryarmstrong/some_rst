helpers/pdas.ts
===============

Last edited: 2023-02-28 18:04:35

Contents:

.. code-block:: ts

    import { PublicKey } from "@solana/web3.js";
import { PROGRAM_ADDRESS } from "@metaplex-foundation/mpl-trifle/dist/src/generated";
import { PROGRAM_ADDRESS as TOKEN_METADATA_PROGRAM_ADDRESS } from "@metaplex-foundation/mpl-token-metadata";

export const findTriflePda = async (
  mint: PublicKey,
  authority: PublicKey,
) => {
  return await PublicKey.findProgramAddress(
    [
      Buffer.from("trifle"),
      mint.toBuffer(),
      authority.toBuffer(),
    ],
    new PublicKey(PROGRAM_ADDRESS),
  );
};

export const findEscrowPda = async (
  mint: PublicKey,
  authority: 0 | 1,
  creator?: PublicKey,
) => {
  let seeds = [
    Buffer.from("metadata"),
    new PublicKey(TOKEN_METADATA_PROGRAM_ADDRESS).toBuffer(),
    mint.toBuffer(),
    Uint8Array.from([authority]),
  ];

  if (authority == 1) {
    if (creator) {
      seeds.push(creator.toBuffer());
    } else {
      throw new Error("Creator is required");
    }
  }

  seeds.push(Buffer.from("escrow"));
  return await PublicKey.findProgramAddress(
    seeds,
    new PublicKey(TOKEN_METADATA_PROGRAM_ADDRESS),
  );
};


