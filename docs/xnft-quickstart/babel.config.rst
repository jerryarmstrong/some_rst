babel.config.js
===============

Last edited: 2023-07-18 02:03:22

Contents:

.. code-block:: js

    module.exports = function(api) {
  api.cache(true);
  return {
    presets: ['babel-preset-expo'],
  };
};


