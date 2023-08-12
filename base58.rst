base58.js
=========

Last edited: 2023-01-05 08:54:11

Contents:

.. code-block:: js

    const base58 = require('bs58');

const key = require(process.argv[2]);

console.log(base58.encode(key));


