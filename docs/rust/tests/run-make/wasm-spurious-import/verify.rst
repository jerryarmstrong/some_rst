tests/run-make/wasm-spurious-import/verify.js
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: js

    const fs = require('fs');
const process = require('process');
const assert = require('assert');
const buffer = fs.readFileSync(process.argv[2]);

let m = new WebAssembly.Module(buffer);
let imports = WebAssembly.Module.imports(m);
console.log('imports', imports);
assert.strictEqual(imports.length, 0);


