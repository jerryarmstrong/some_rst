example/babel.config.js
=======================

Last edited: 2023-03-28 15:16:55

Contents:

.. code-block:: js

    const path = require('path');
module.exports = function (api) {
  api.cache(true);
  return {
    presets: ['babel-preset-expo'],
    plugins: [
      [
        'module-resolver',
        {
          extensions: ['.tsx', '.ts', '.js', '.json'],
          alias: {
            // For development, we want to alias the library to the source
            'expo-mobile-wallet-adapter': path.join(__dirname, '..', 'src', 'index.ts'),
          },
        },
      ],
    ],
  };
};


