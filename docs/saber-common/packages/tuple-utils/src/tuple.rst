packages/tuple-utils/src/tuple.ts
=================================

Last edited: 2023-06-29 16:13:38

Contents:

.. code-block:: ts

    /**
 * A tuple of length `N` with elements of type `T`.
 */
export type Tuple<T, N extends number> = N extends N
  ? number extends N
    ? T[]
    : _TupleOf<T, N, []>
  : never;
type _TupleOf<T, N extends number, R extends unknown[]> = R["length"] extends N
  ? R
  : _TupleOf<T, N, [T, ...R]>;


