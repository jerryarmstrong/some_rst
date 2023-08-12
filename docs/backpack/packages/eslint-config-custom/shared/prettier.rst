packages/eslint-config-custom/shared/prettier.js
================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: js

    // MAKE SURE YOU INSTALL eslint-plugin-prettier for this to work
module.exports = {
  extends: ["prettier"],
  plugins: ["prettier"],
  rules: {
    "prettier/prettier": ["warn"],
  },
};


