tools/core/script.ts
====================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    // Converts array of items to a Map
export function arrayToMap<T, K>(source: readonly T[], getKey: (item: T) => K) {
  return new Map(source.map((item) => [getKey(item), item] as [K, T]))
}

export function arrayToRecord<T>(
  source: readonly T[],
  getKey: (item: T) => string
) {
  return source.reduce((all, a) => ({ ...all, [getKey(a)]: a }), {}) as Record<
    string,
    T
  >
}

export function getNameOf<T>() {
  return (name: keyof T) => name
}


