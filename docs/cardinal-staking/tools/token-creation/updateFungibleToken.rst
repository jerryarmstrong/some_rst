tools/token-creation/updateFungibleToken.ts
===========================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { findMintMetadataId } from "@cardinal/common";
import { utils } from "@coral-xyz/anchor";
import { createCreateMetadataAccountV3Instruction } from "@metaplex-foundation/mpl-token-metadata";
import {
  Keypair,
  PublicKey,
  sendAndConfirmRawTransaction,
  Transaction,
} from "@solana/web3.js";

import { connectionFor } from "../connection";

const wallet = Keypair.fromSecretKey(
  utils.bytes.bs58.decode(process.env.AIRDROP_KEY || "")
);

const MINT_PUBLIC_KEY = new PublicKey("");

export const updateFungibleToken = async (cluster = "devnet") => {
  const connection = connectionFor(cluster);
  try {
    const metadataId = findMintMetadataId(MINT_PUBLIC_KEY);
    const metadataIx = createCreateMetadataAccountV3Instruction(
      {
        metadata: metadataId,
        mint: MINT_PUBLIC_KEY,
        mintAuthority: wallet.publicKey,
        payer: wallet.publicKey,
        updateAuthority: wallet.publicKey,
      },
      {
        createMetadataAccountArgsV3: {
          isMutable: true,
          collectionDetails: null,
          data: {
            name: "",
            symbol: "",
            uri: "",
            sellerFeeBasisPoints: 0,
            creators: [
              {
                address: wallet.publicKey,
                verified: true,
                share: 100,
              },
            ],
            collection: null,
            uses: null,
          },
        },
      }
    );
    const transaction = new Transaction();
    transaction.add(metadataIx);
    transaction.feePayer = wallet.publicKey;
    transaction.recentBlockhash = (
      await connection.getRecentBlockhash("max")
    ).blockhash;
    transaction.sign(wallet);
    const txid = await sendAndConfirmRawTransaction(
      connection,
      transaction.serialize(),
      {
        commitment: "confirmed",
      }
    );
    console.log(
      `Token updated mintId=(${MINT_PUBLIC_KEY.toString()}) metadataId=(${metadataId.toString()}) with transaction https://explorer.solana.com/tx/${txid}?cluster=${cluster}`
    );
  } catch (e) {
    console.log("Failed", e);
  }
};

updateFungibleToken().catch((e) => {
  console.log(e);
});


