src/util/sleep.js
=================

Last edited: 2020-06-24 17:49:11

Contents:

.. code-block:: js

    // @flow

// zzz
export function sleep(ms: number): Promise<void> {
  return new Promise(resolve => setTimeout(resolve, ms));
}


