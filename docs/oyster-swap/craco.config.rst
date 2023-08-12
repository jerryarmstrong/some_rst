craco.config.js
===============

Last edited: 2020-11-17 14:49:57

Contents:

.. code-block:: js

    const CracoLessPlugin = require("craco-less");

module.exports = {
  plugins: [
    {
      plugin: CracoLessPlugin,
      options: {
        lessLoaderOptions: {
          lessOptions: {
            modifyVars: { "@primary-color": "#2abdd2" },
            javascriptEnabled: true,
          },
        },
      },
    },
  ],
};


