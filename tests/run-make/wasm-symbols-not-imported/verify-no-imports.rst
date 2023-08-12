tests/run-make/wasm-symbols-not-imported/verify-no-imports.js
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: js

    const fs = require('fs');
const process = require('process');
const assert = require('assert');
const buffer = fs.readFileSync(process.argv[2]);

let m = new WebAssembly.Module(buffer);
let list = WebAssembly.Module.imports(m);
console.log('imports', list);
if (list.length !== 0)
  throw new Error("there are some imports");


