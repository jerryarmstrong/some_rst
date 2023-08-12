webpack.main.config.js
======================

Last edited: 2020-07-22 13:30:11

Contents:

.. code-block:: js

    const rules = require('./webpack.rules');

module.exports = {
  entry: './src/index.js',
  module: {
    rules,
  },
};


