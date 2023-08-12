packages/library-legacy/src/utils/sleep.ts
==========================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    // zzz
export function sleep(ms: number): Promise<void> {
  return new Promise(resolve => setTimeout(resolve, ms));
}


