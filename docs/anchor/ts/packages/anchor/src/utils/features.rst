ts/packages/anchor/src/utils/features.ts
========================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: ts

    const _AVAILABLE_FEATURES = new Set(["anchor-deprecated-state", "debug-logs"]);

const _FEATURES = new Map();

export function set(key: string) {
  if (!_AVAILABLE_FEATURES.has(key)) {
    throw new Error("Invalid feature");
  }
  _FEATURES.set(key, true);
}

export function isSet(key: string): boolean {
  return _FEATURES.get(key) !== undefined;
}


