webpack.config.dev-server.js
============================

Last edited: 2023-05-04 20:47:44

Contents:

.. code-block:: js

    const { merge } = require('webpack-merge');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const commonConfig = require('./webpack.config.common.js');

module.exports = merge(commonConfig, {
  mode: 'development',
  devServer: {
    injectClient: false //workaround for bug https://github.com/webpack/webpack-dev-server/issues/2484
  },
  devtool: "inline-source-map",
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html',
      inject: 'head'
    })
  ]
});


