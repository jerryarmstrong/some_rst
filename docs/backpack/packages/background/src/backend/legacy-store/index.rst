packages/background/src/backend/legacy-store/index.ts
=====================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    // This "store" module defines all the persistent model objects for the storage
// layer of the app.

import { LocalStorageDb } from "./db";

export * from "./feature-gates";
export * from "./navigation";
export * from "./xnft-preferences";

export function reset() {
  return LocalStorageDb.reset();
}


