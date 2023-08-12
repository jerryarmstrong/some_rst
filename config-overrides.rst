config-overrides.js
===================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    /* eslint-disable */
const {override, addBabelPlugin, addWebpackPlugin} = require('customize-cra');
const webpack = require('webpack');

module.exports = override(
  // addBabelPlugin('lodash'),
  addBabelPlugin('react-hot-loader/babel'),
  addBabelPlugin('date-fns'),
  addWebpackPlugin(new webpack.ContextReplacementPlugin(/hasha/)),
);


