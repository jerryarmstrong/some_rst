packages/umi-serializers/src/maxSerializerSizes.ts
==================================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    export function maxSerializerSizes(sizes: (number | null)[]): number | null {
  return sizes.reduce(
    (all, size) => (all === null || size === null ? null : Math.max(all, size)),
    0 as number | null
  );
}


