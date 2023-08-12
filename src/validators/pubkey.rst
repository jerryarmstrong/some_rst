src/validators/pubkey.ts
========================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: ts

    import { coerce, instance, string } from "superstruct";
import { PublicKey } from "@solana/web3.js";

export const PublicKeyFromString = coerce(
  instance(PublicKey),
  string(),
  (value) => new PublicKey(value)
);


