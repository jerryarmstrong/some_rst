token-swap/js/client/util/sleep.js
==================================

Last edited: 2020-08-26 08:56:56

Contents:

.. code-block:: js

    // @flow

// zzz
export function sleep(ms: number): Promise<void> {
  return new Promise(resolve => setTimeout(resolve, ms));
}


