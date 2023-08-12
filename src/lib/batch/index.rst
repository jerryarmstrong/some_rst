src/lib/batch/index.ts
======================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    export function batch<T>(items: T[], batchSize = 100): T[][] {
  if (items.length <= batchSize) {
    return [items]
  }

  const some = items.slice(0, batchSize)
  const rest = items.slice(batchSize)

  return [some, ...batch(rest, batchSize)]
}


