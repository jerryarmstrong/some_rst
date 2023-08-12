packages/tuple-utils/src/fill.ts
================================

Last edited: 2023-06-29 16:13:38

Contents:

.. code-block:: ts

    import type { Tuple } from "./tuple.js";

/**
 * Replaces all of the values of a tuple with the given value.
 */
export const tupleFill = <V, N extends number, T>(
  value: V,
  tuple: Tuple<T, N>
): Tuple<V, N> => {
  return tuple.map(() => value) as Tuple<V, N>;
};


