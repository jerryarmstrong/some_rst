src/sleep.js
============

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    // @flow

// zzz
export function sleep(ms: number): Promise<void> {
  return new Promise(resolve => setTimeout(resolve, ms));
}


