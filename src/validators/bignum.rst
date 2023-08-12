src/validators/bignum.ts
========================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: ts

    import { coerce, instance, string } from "superstruct";
import BN from "bn.js";

export const BigNumFromString = coerce(instance(BN), string(), (value) => {
  if (typeof value === "string") return new BN(value, 10);
  throw new Error("invalid big num");
});


