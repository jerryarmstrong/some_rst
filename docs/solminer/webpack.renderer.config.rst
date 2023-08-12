webpack.renderer.config.js
==========================

Last edited: 2020-07-22 13:30:11

Contents:

.. code-block:: js

    const path = require('path');
const rules = require('./webpack.rules');

module.exports = {
  resolve: {
    extensions: ['.js', '.jsx'],
    alias: {
      'react-dom': '@hot-loader/react-dom',
      styles: path.resolve(__dirname, './src/styles'),
    },
  },
  module: {
    rules,
  },
};


