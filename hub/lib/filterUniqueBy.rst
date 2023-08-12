hub/lib/filterUniqueBy.ts
=========================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    export function filterUniqueBy<O extends object, K extends keyof O>(key: K) {
  const visited = new Set<O[K]>();

  return (o: O) => {
    const itemKey = o[key];

    if (visited.has(itemKey)) {
      return false;
    }

    return true;
  };
}


