src/sleep.js
============

Last edited: 2020-07-22 13:30:11

Contents:

.. code-block:: js

    export default function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}


