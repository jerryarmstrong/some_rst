expo-managed-mwa/babel.config.js
================================

Last edited: 2023-02-17 20:13:33

Contents:

.. code-block:: js

    module.exports = function(api) {
  api.cache(true);
  return {
    presets: ['babel-preset-expo']
  };
};


