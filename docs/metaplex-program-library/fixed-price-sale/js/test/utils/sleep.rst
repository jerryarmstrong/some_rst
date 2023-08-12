fixed-price-sale/js/test/utils/sleep.ts
=======================================

Last edited: 2023-07-31 23:00:16

Contents:

.. code-block:: ts

    export function sleep(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}


