packages/recoil/src/utils.ts
============================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    export function isPromise(p: any): p is Promise<any> {
  return !!p && typeof p.then === "function";
}


