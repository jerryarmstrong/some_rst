utils/group.ts
==============

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    export default function group<T>(items: T[], groupSize = 100): T[][] {
  if (items.length <= groupSize) {
    return [items]
  }

  const some = items.slice(0, groupSize)
  const rest = items.slice(groupSize)

  return [some, ...group(rest, groupSize)]
}


