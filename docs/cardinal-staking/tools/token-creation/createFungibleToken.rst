tools/token-creation/createFungibleToken.ts
===========================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { findMintMetadataId } from "@cardinal/common";
import { utils } from "@coral-xyz/anchor";
import { createCreateMetadataAccountV2Instruction } from "@metaplex-foundation/mpl-token-metadata";
import {
  createAssociatedTokenAccountInstruction,
  createInitializeMint2Instruction,
  createMintToInstruction,
  getAssociatedTokenAddressSync,
  getMinimumBalanceForRentExemptMint,
  MINT_SIZE,
  TOKEN_PROGRAM_ID,
} from "@solana/spl-token";
import {
  Keypair,
  sendAndConfirmRawTransaction,
  SystemProgram,
  Transaction,
} from "@solana/web3.js";

import { connectionFor } from "../connection";

const wallet = Keypair.fromSecretKey(
  utils.bytes.bs58.decode(process.env.AIRDROP_KEY || "")
);

const MINT_KEYPAIR = Keypair.fromSecretKey(
  utils.bytes.bs58.decode(process.env.AIRDROP_KEY || "")
);

const SUPPLY = 60_000_000_0000000;
const DECIMALS = 7;

export const createFungibleToken = async (
  cluster = "devnet",
  mintKeypair: Keypair
) => {
  const connection = connectionFor(cluster);
  try {
    const tokenAccountId = getAssociatedTokenAddressSync(
      mintKeypair.publicKey,
      wallet.publicKey
    );
    const metadataId = findMintMetadataId(mintKeypair.publicKey);

    const transaction = new Transaction().add(
      SystemProgram.createAccount({
        fromPubkey: wallet.publicKey,
        newAccountPubkey: mintKeypair.publicKey,
        space: MINT_SIZE,
        lamports: await getMinimumBalanceForRentExemptMint(connection),
        programId: TOKEN_PROGRAM_ID,
      }),
      createInitializeMint2Instruction(
        mintKeypair.publicKey,
        DECIMALS,
        wallet.publicKey,
        wallet.publicKey
      ),
      createAssociatedTokenAccountInstruction(
        wallet.publicKey,
        tokenAccountId,
        wallet.publicKey,
        mintKeypair.publicKey
      ),
      createMintToInstruction(
        mintKeypair.publicKey,
        tokenAccountId,
        wallet.publicKey,
        SUPPLY
      ),
      createCreateMetadataAccountV2Instruction(
        {
          metadata: metadataId,
          mint: mintKeypair.publicKey,
          updateAuthority: wallet.publicKey,
          mintAuthority: wallet.publicKey,
          payer: wallet.publicKey,
        },
        {
          createMetadataAccountArgsV2: {
            data: {
              name: `name-${Math.random()}`,
              symbol: "SYMB",
              uri: `uri-${Math.random()}`,
              sellerFeeBasisPoints: 0,
              creators: [
                { address: wallet.publicKey, share: 100, verified: true },
              ],
              collection: null,
              uses: null,
            },
            isMutable: true,
          },
        }
      )
    );
    transaction.feePayer = wallet.publicKey;
    transaction.recentBlockhash = (
      await connection.getRecentBlockhash("max")
    ).blockhash;
    transaction.sign(wallet, mintKeypair);
    const txid = await sendAndConfirmRawTransaction(
      connection,
      transaction.serialize(),
      {
        commitment: "confirmed",
      }
    );
    console.log(
      `Token created mintId=(${mintKeypair.publicKey.toString()}) metadataId=(${metadataId.toString()}) tokenAccount=(${tokenAccountId.toString()}) with transaction https://explorer.solana.com/tx/${txid}?cluster=${cluster}`
    );
  } catch (e) {
    console.log("Failed", e);
  }
};

createFungibleToken("mainnet", MINT_KEYPAIR).catch((e) => {
  console.log(e);
});


