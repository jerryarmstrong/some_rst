postcss.config.js
=================

Last edited: 2023-08-11 10:00:06

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


