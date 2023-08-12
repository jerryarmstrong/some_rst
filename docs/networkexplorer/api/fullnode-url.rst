api/fullnode-url.js
===================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    // export const FULLNODE_URL = 'http://beta.testnet.solana.com:8899';
export const FULLNODE_URL = process.env.FULLNODE_URL || 'http://localhost:8899';


