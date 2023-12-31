packages/recoil/src/atoms/solana/isONELive.tsx
==============================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { Blockchain } from "@coral-xyz/common";
import { selector } from "recoil";

import { authenticatedUser } from "../preferences";
import { activeWallet } from "../wallet";

export const isOneLive = selector<{
  isLive: boolean;
  wlCollection?: string;
  madladsCollection?: string;
  banner?: string;
  hasMadladBanner?: string;
  hasWLBanner?: string;
}>({
  key: "isOneLive",
  get: async ({ get }) => {
    const wallet = get(activeWallet);
    if (wallet?.blockchain !== Blockchain.SOLANA) {
      return { isLive: false };
    }
    return (
      fetch("https://one.xnfts.dev/api/isLive?wallet=" + wallet.publicKey)
        // return fetch("http://localhost:3000/api/isLive")
        .then((r) => r.json())
        .catch(() => ({ isLive: false }))
    );
  },
});


