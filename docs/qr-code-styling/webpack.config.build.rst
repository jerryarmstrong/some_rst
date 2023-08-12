webpack.config.build.js
=======================

Last edited: 2023-05-04 20:47:44

Contents:

.. code-block:: js

    const commonConfig = require('./webpack.config.common.js');
const config = commonConfig;

module.exports = (env, argv) => {
  config.mode = argv.mode;

  if (argv.mode === "development") {
    config.devtool = "inline-source-map";
    config.watch = true;
  }

  if (argv.mode === "production") {
    config.devtool = "source-map";
  }

  return config;
};

