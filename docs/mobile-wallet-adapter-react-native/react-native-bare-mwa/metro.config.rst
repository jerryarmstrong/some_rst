react-native-bare-mwa/metro.config.js
=====================================

Last edited: 2023-02-17 20:13:33

Contents:

.. code-block:: js

    /**
 * Metro configuration for React Native
 * https://github.com/facebook/react-native
 *
 * @format
 */

module.exports = {
  transformer: {
    getTransformOptions: async () => ({
      transform: {
        experimentalImportSupport: false,
        inlineRequires: true,
      },
    }),
  },
};


