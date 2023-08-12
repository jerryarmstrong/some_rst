index.js
========

Last edited: 2023-07-15 04:41:58

Contents:

.. code-block:: js

    const base = require("./base.js");
module.exports = {
  ...base,
  extends: ["eslint:recommended", "plugin:@typescript-eslint/recommended"],
  plugins: [...base.plugins, "sort-keys-fix"],
  rules: {
    ...base.rules,
    "@typescript-eslint/no-unused-vars": [
      "error",
      {
        argsIgnorePattern: "^_",
        destructuredArrayIgnorePattern: "^_",
      },
    ],
    "no-unused-vars": "off",
  },
};


