app/packages/twamm-types/lib/twamm-types.ts
===========================================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: ts

    import type { Provider } from "@project-serum/anchor";
import type { PublicKey } from "@solana/web3.js";

export enum OrderSide {
  "sell" = "sell",
  "buy" = "buy",
  "defaultSide" = "sell",
}

export interface WalletProvider extends Provider {
  wallet: { publicKey: PublicKey };
}


