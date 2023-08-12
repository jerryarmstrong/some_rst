packages/eslint-config-custom/web.js
====================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: js

    module.exports = {
  extends: ["./shared/core.js", "./shared/typescript.js", "./shared/react.js"],
  env: { browser: true, commonjs: true },
  plugins: ["mui-unused-classes"],
  rules: {
    "mui-unused-classes/unused-classes": "error",
  },
};


