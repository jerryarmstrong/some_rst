packages/eslint-config-custom/index.js
======================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: js

    module.exports = {
    extends: ['next', 'turbo', 'prettier'],
    rules: {
        '@next/next/no-html-link-for-pages': 'off',
    },
};


