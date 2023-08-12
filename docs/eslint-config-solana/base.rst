base.js
=======

Last edited: 2023-07-15 04:41:58

Contents:

.. code-block:: js

    module.exports = {
  env: {
    es2020: true,
    "shared-node-browser": true,
  },
  ignorePatterns: ["dist/**", "lib/**"],
  parser: "@typescript-eslint/parser",
  plugins: [
    "@typescript-eslint",
    'simple-import-sort',
  ],
  parserOptions: {
    sourceType: "module",
  },
  rules: {
    "simple-import-sort/imports": "error",
    "sort-keys-fix/sort-keys-fix": "error",
  }
};


