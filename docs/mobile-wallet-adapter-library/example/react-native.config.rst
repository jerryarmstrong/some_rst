example/react-native.config.js
==============================

Last edited: 2023-03-27 15:10:41

Contents:

.. code-block:: js

    const path = require('path');
const pak = require('../package.json');

module.exports = {
  dependencies: {
    [pak.name]: {
      root: path.join(__dirname, '..'),
    },
  },
};


