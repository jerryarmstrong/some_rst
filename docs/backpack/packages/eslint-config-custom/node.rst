packages/eslint-config-custom/node.js
=====================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: js

    module.exports = {
  extends: ["./shared/core.js", "./shared/typescript.js"],
  plugins: ["node"],
  env: { node: true },
  rules: {
    "no-buffer-constructor": "warn",
    "node/no-path-concat": "warn",
  },
};


