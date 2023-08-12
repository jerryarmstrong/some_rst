docs/postcss.config.js
======================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: js

    module.exports = {
  plugins: {
    'postcss-import': {},
    tailwindcss: {},
    'postcss-focus-visible': {
      replaceWith: '[data-focus-visible-added]',
    },
    autoprefixer: {},
  },
}


