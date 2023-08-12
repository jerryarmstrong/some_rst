examples/clients/simple/src/solana/SignMessageButton.tsx
========================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import type { FC } from "react";
import React, { useCallback } from "react";
import * as anchor from "@project-serum/anchor";
import { WalletNotConnectedError } from "@solana/wallet-adapter-base";
import { useConnection, useWallet } from "@solana/wallet-adapter-react";

export const SignMessageButton: FC = () => {
  const { connection } = useConnection();
  const wallet = useWallet();
  const onClick = useCallback(async () => {
    if (!wallet.publicKey) throw new WalletNotConnectedError();

    const msg = anchor.utils.bytes.utf8.encode("hello world");
    console.log("requesting sig over", msg);
    const signature = await wallet.signMessage!(msg);
    console.log("signature", signature);
  }, [wallet.publicKey, wallet.sendTransaction, connection]);

  return (
    <button onClick={onClick} disabled={!wallet.publicKey}>
      Sign the message: "hello world"
    </button>
  );
};


