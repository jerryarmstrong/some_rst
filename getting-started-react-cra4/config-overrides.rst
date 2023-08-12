getting-started-react-cra4/config-overrides.js
==============================================

Last edited: 2023-05-10 12:33:36

Contents:

.. code-block:: js

    module.exports = function override(webpackConfig) {
  webpackConfig.module.rules.push({
    test: /\.mjs$/,
    include: /node_modules/,
    type: "javascript/auto",
  });
  return webpackConfig;
};


