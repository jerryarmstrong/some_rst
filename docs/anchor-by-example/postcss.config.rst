postcss.config.js
=================

Last edited: 2022-08-19 10:41:17

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


