packages/test-config/test-validator-teardown.js
===============================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: js

    /* eslint-disable */
const { teardown } = require('jest-dev-server');

module.exports = async function globalTeardown() {
    await teardown(globalThis.servers);
};


