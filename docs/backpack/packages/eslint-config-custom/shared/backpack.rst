packages/eslint-config-custom/shared/backpack.js
================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: js

    module.exports = {
  rules: {
    "no-restricted-imports": [
      "error",
      {
        name: "@coral-xyz/app-extension",
        message:
          "dont import app-extension into shared modules bc of build tooling",
      },
      {
        name: "@coral-xyz/app-mobile",
        message:
          "dont import app-mobile into shared modules bc of build tooling",
      },
    ],
  },
};


