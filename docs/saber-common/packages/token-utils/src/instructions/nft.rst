packages/token-utils/src/instructions/nft.ts
============================================

Last edited: 2023-06-29 16:13:38

Contents:

.. code-block:: ts

    import type { Provider, TransactionEnvelope } from "@saberhq/solana-contrib";
import { AuthorityType, createMintToInstruction,createSetAuthorityInstruction, TOKEN_PROGRAM_ID } from "@solana/spl-token";
import { u64} from "@solana/buffer-layout-utils";
import type { PublicKey, Signer } from "@solana/web3.js";

import { getOrCreateATA } from "./ata.js";
import { createInitMintInstructions } from "./mint.js";

export const mintNFT = async (
  provider: Provider,
  mintKP: Signer,
  owner: PublicKey = provider.wallet.publicKey
): Promise<TransactionEnvelope> => {
  // Temporary mint authority
  const tempMintAuthority = provider.wallet.publicKey;
  // Mint for the NFT
  const tx = await createInitMintInstructions({
    provider,
    mintKP,
    decimals: 0,
    mintAuthority: tempMintAuthority,
  });
  // Token account for the NFT
  const { address, instruction } = await getOrCreateATA({
    provider,
    mint: mintKP.publicKey,
    owner: owner,
    payer: provider.wallet.publicKey,
  });
  if (instruction) {
    tx.instructions.push(instruction);
  }
  // Mint to owner's ATA
  tx.instructions.push(
    // SPLToken.createMintToInstruction(
    //   TOKEN_PROGRAM_ID,
    //   mintKP.publicKey,
    //   address,
    //   tempMintAuthority,
    //   [],
    //   new u64(1)
    // )
    createMintToInstruction(
      mintKP.publicKey,
      address,
      tempMintAuthority,
      new u64(1),
      [],
      TOKEN_PROGRAM_ID,
    )
  );
  // Set mint authority of the NFT to NULL
  tx.instructions.push(
    // SPLToken.createSetAuthorityInstruction(
    //   TOKEN_PROGRAM_ID,
    //   mintKP.publicKey,
    //   null,
    //   "MintTokens",
    //   tempMintAuthority,
    //   []
    // )
    createSetAuthorityInstruction(
      mintKP.publicKey,
      tempMintAuthority,
      AuthorityType.MintTokens,
      null,
      [],
      TOKEN_PROGRAM_ID
    )
  );

  return tx;
};


