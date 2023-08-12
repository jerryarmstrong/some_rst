.yarn/sdks/eslint/lib/api.js
============================

Last edited: 2023-06-29 16:13:38

Contents:

.. code-block:: js

    #!/usr/bin/env node

const {existsSync} = require(`fs`);
const {createRequire} = require(`module`);
const {resolve} = require(`path`);

const relPnpApiPath = "../../../../.pnp.cjs";

const absPnpApiPath = resolve(__dirname, relPnpApiPath);
const absRequire = createRequire(absPnpApiPath);

if (existsSync(absPnpApiPath)) {
  if (!process.versions.pnp) {
    // Setup the environment to be able to require eslint
    require(absPnpApiPath).setup();
  }
}

// Defer to the real eslint your application uses
module.exports = absRequire(`eslint`);


