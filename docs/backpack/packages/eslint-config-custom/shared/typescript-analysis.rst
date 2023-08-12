packages/eslint-config-custom/shared/typescript-analysis.js
===========================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: js

    module.exports = {
  extends: ["./typescript.js"],
  overrides: [
    {
      files: ["*.ts", "*.tsx", "*.d.ts"],
      rules: {
        "@typescript-eslint/no-for-in-array": "error",
        "@typescript-eslint/no-throw-literal": "warn",
        "@typescript-eslint/prefer-nullish-coalescing": "warn",
        "@typescript-eslint/prefer-optional-chain": "warn",
      },
    },
  ],
};


