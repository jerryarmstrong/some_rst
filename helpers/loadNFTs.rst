helpers/loadNFTs.ts
===================

Last edited: 2023-02-28 18:04:35

Contents:

.. code-block:: ts

    import { Metadata, Metaplex } from "@metaplex-foundation/js";
import { WalletContextState } from "@solana/wallet-adapter-react";
import { findTriflePda } from "./pdas";

export const loadNFTs = async (
  metaplex: Metaplex,
  wallet: WalletContextState,
) => {
  const lazyNfts = await metaplex.nfts().findAllByOwner({
    owner: wallet.publicKey!,
  });
  const nftPromises = lazyNfts.map((nft) => {
    return metaplex.nfts().findByMint({
      mintAddress: (nft as Metadata).mintAddress,
    });
  });

  return await Promise.all(nftPromises);
};

export const loadTrifleNFTs = async (metaplex: Metaplex, wallet: WalletContextState) => {
  const nfts = await loadNFTs(metaplex, wallet);
  let trifleNFTs = [];
  for (let i = 0; i < nfts.length; i++) {
    let nft = nfts[i];
    let trifleAddress = await findTriflePda(nft.address, nft.updateAuthorityAddress);
    let account = await metaplex.connection.getAccountInfo(trifleAddress[0]);
    console.log(account);
    if (account) {
      trifleNFTs.push(nft);
    }
  }
  return trifleNFTs;
};

