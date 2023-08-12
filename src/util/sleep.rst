src/util/sleep.js
=================

Last edited: 2020-05-08 23:31:17

Contents:

.. code-block:: js

    // @flow

// zzz
export function sleep(ms: number): Promise<void> {
  return new Promise(resolve => setTimeout(resolve, ms));
}


