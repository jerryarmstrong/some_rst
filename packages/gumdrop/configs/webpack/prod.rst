packages/gumdrop/configs/webpack/prod.js
========================================

Last edited: 2022-08-25 19:21:42

Contents:

.. code-block:: js

    // production config
const { merge } = require("webpack-merge");
const { resolve } = require("path");

const commonConfig = require("./common");

module.exports = merge(commonConfig, {
  mode: "production",
  entry: "./index.tsx",
  output: {
    filename: "js/bundle.[contenthash].min.js",
    path: resolve(__dirname, "../../dist"),
  },
  devtool: "source-map",
  plugins: [],
});


