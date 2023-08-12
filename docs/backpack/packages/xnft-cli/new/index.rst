packages/xnft-cli/new/index.js
==============================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: js

    const bundle = require("./bundle");
const dev = require("./dev");

module.exports = (program) => {
  program.description("CLI for xnfts");
  bundle(program);
  dev(program);
};


