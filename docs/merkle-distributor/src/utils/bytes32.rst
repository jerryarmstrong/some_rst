src/utils/bytes32.ts
====================

Last edited: 2023-05-25 13:38:49

Contents:

.. code-block:: ts

    import invariant from "tiny-invariant";

export const toBytes32Array = (b: Buffer): number[] => {
  invariant(b.length <= 32, `invalid length ${b.length}`);
  const buf = Buffer.alloc(32);
  b.copy(buf, 32 - b.length);

  return Array.from(buf);
};


