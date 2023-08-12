packages/app-mobile/relay.config.js
===================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: js

    // relay.config.js
module.exports = {
  // ...
  // Configuration options accepted by the `relay-compiler` command-line tool and `babel-plugin-relay`.
  src: "./src",
  language: "typescript", // "javascript" | "typescript" | "flow"
  schema: "../../backend/native/backpack-api/src/schema.graphql",
  exclude: ["**/node_modules/**", "**/__mocks__/**", "**/__generated__/**"],
};


