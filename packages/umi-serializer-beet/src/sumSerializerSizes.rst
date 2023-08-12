packages/umi-serializer-beet/src/sumSerializerSizes.ts
======================================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    export function sumSerializerSizes(sizes: (number | null)[]): number | null {
  return sizes.reduce(
    (all, size) => (all === null || size === null ? null : all + size),
    0 as number | null
  );
}


