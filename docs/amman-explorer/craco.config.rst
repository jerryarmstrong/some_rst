craco.config.js
===============

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: js

    const webpack = require('webpack')

/**
 * Fallbacks are required due to webpack 5 no longer supplying node polyfills by default
 * Rather than eject from CRA, we use craco to patch in what we need. What is included here is
 * only what is required to resolve all compiler errors.
 * See https://github.com/facebook/create-react-app/issues/11756
 */

module.exports = {
  webpack: {
    configure: {
      module: {
        rules: [
          {
            test: /\.m?js/,
            resolve: {
              fullySpecified: false,
            },
          },
        ],
      },
      ignoreWarnings: [/Failed to parse source map/],
      resolve: {
        fallback: {
          process: false, // require.resolve('process/browser'),
          crypto: require.resolve('crypto-browserify'),
          stream: require.resolve('stream-browserify'),
          http: false, // require.resolve("stream-http")
          https: false, // require.resolve("https-browserify")
          fs: false,
          os: false,
          assert: require.resolve('assert'),
          path: require.resolve('path-browserify'),
        },
      },
      plugins: [
        new webpack.ProvidePlugin({
          Buffer: ['buffer', 'Buffer'],
          process: 'process/browser',
        }),
      ],
    },
  },
}


