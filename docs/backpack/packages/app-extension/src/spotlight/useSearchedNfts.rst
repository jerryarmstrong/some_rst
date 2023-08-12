packages/app-extension/src/spotlight/useSearchedNfts.tsx
========================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import type { Nft } from "@coral-xyz/common";
import { Blockchain } from "@coral-xyz/common";
import { nftsByOwner, useActiveSolanaWallet } from "@coral-xyz/recoil";
import { useRecoilValueLoadable } from "recoil";

export const useSearchedNfts = (searchFilter: string) => {
  const activeSolWallet = useActiveSolanaWallet();
  const { contents, state }: any = useRecoilValueLoadable(
    nftsByOwner({
      publicKey: activeSolWallet?.publicKey,
      blockchain: Blockchain.SOLANA,
    })
  );

  if (state === "loading" || state === "hasError") {
    return [];
  }

  return contents
    .filter(
      (x: Nft) =>
        x &&
        (x.name?.toLowerCase()?.includes(searchFilter.toLowerCase()) ||
          x.collectionName?.toLowerCase()?.includes(searchFilter.toLowerCase()))
    )
    .map((x: Nft) => ({
      name: x.name || "",
      image: x.imageUrl || "",
      id: x.id || "",
    }));
};


