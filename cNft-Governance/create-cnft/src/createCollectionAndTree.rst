cNft-Governance/create-cnft/src/createCollectionAndTree.ts
==========================================================

Last edited: 2023-07-14 15:51:14

Contents:

.. code-block:: ts

    import { createCollection } from "../utils/create-collection";
import { createMerkleTree } from "../utils/create-tree";
import { Keypair, Connection } from "@solana/web3.js";
import {
  Metaplex,
  keypairIdentity,
  bundlrStorage,
  toMetaplexFile,
  UploadMetadataInput,
} from "@metaplex-foundation/js";

import { CreateMetadataAccountArgsV3 } from "@metaplex-foundation/mpl-token-metadata";
import * as fs from "fs";
import dotenv from "dotenv";
dotenv.config();

(async () => {
  const payer = Keypair.fromSecretKey(
    Uint8Array.from(JSON.parse(process.env.PRIVATE_KEY ?? "[]"))
  );
  console.log("payer: ", payer.publicKey.toBase58());

  const connection = new Connection(process.env.RPC_URL ?? "", "confirmed");
  const balance = await connection.getBalance(payer.publicKey);
  console.log("balance: ", balance);

  const metaplex = Metaplex.make(connection)
    .use(keypairIdentity(payer))
    .use(
      bundlrStorage({
        address: "https://devnet.bundlr.network",
        providerUrl: "https://api.devnet.solana.com",
        timeout: 60000,
      })
    );

  // Create collection metadata
  const buffer = fs.readFileSync("./src/assets/collection.jpeg");
  const file = toMetaplexFile(buffer, "collection.jpeg");
  const imageUri = await metaplex.storage().upload(file);

  const data = fs.readFileSync("./src/collection.json", "utf-8");
  const collectionInfo = JSON.parse(data);

  const collectionMetadata: UploadMetadataInput = {
    name: collectionInfo.name,
    symbol: collectionInfo.symbol,
    image: imageUri,
    description: collectionInfo.description,
  };
  const { uri } = await metaplex.nfts().uploadMetadata(collectionMetadata);

  // Create collection
  const collectionMetadataV3: CreateMetadataAccountArgsV3 = {
    data: {
      name: collectionMetadata.name ?? "",
      symbol: collectionMetadata.symbol ?? "",
      uri,
      sellerFeeBasisPoints: 100,
      creators: [
        {
          address: payer.publicKey,
          verified: true,
          share: 100,
        },
      ],
      collection: null,
      uses: null,
    },
    isMutable: false,
    collectionDetails: null,
  };

  const collection = await createCollection(
    connection,
    payer,
    collectionMetadataV3
  );

  // create tree space for compressed nft
  const treeKeypair = Keypair.generate();
  const tree = await createMerkleTree(connection, payer, treeKeypair);
})();


