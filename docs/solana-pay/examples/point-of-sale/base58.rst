examples/point-of-sale/base58.js
================================

Last edited: 2023-05-03 15:27:33

Contents:

.. code-block:: js

    const base58 = require('bs58');

const key = require(process.argv[2]);

console.log(base58.encode(key));


