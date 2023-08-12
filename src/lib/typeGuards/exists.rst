src/lib/typeGuards/exists.ts
============================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    /**
 * Determines if an item is not null or undefined
 */
export function exists<T>(item: T | null | undefined): item is T {
  return item !== null && item !== undefined;
}


