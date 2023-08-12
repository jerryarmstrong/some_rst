packages/recoil/src/atoms/solana/wallet.tsx
===========================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { BackgroundSolanaConnection, TokenInterface } from "@coral-xyz/common";
import { AnchorProvider } from "@project-serum/anchor";
import { Keypair } from "@solana/web3.js";
import { selector } from "recoil";

import { connectionBackgroundClient } from "../client";

import { solanaCommitment, solanaConnectionUrl } from "./preferences";

export const anchorContext = selector({
  key: "anchorContext",
  get: ({ get }: any) => {
    const _connectionUrl = get(solanaConnectionUrl);
    const _connectionBackgroundClient = get(connectionBackgroundClient);
    const connection = new BackgroundSolanaConnection(
      _connectionBackgroundClient,
      _connectionUrl
    );
    const _commitment = get(solanaCommitment);
    //
    // Note: this provider is *read-only*.
    //
    const dummyWallet = Keypair.generate();
    // @ts-ignore
    const provider = new AnchorProvider(connection, dummyWallet, {
      skipPreflight: false,
      commitment: _commitment,
      preflightCommitment: _commitment,
    });
    const tokenInterface = new TokenInterface(provider);
    return {
      connection,
      connectionUrl: _connectionUrl,
      provider,
      tokenInterface,
    };
  },
});


