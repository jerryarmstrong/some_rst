src/util/sleep.js
=================

Last edited: 2020-07-29 22:45:43

Contents:

.. code-block:: js

    // @flow

// zzz
export function sleep(ms: number): Promise<void> {
  return new Promise(resolve => setTimeout(resolve, ms));
}


