rescript-monaco.js
==================

Last edited: 2023-01-27 22:22:52

Contents:

.. code-block:: js

    const MonacoWebpackPlugin = require("monaco-editor-webpack-plugin");
const { prependWebpackPlugin } = require("@rescripts/utilities");

module.exports = function override(config, env) {
  return prependWebpackPlugin(new MonacoWebpackPlugin({
    // available options are documented at https://github.com/Microsoft/monaco-editor-webpack-plugin#options
    languages: ["json"]
  }), config);
}


