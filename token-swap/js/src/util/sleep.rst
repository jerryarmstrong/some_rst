token-swap/js/src/util/sleep.ts
===============================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: ts

    export function sleep(ms: number): Promise<void> {
  return new Promise(resolve => setTimeout(resolve, ms));
}


