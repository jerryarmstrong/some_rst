packages/app-extension/jest.setup.js
====================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: js

    require("isomorphic-fetch");
const { setDefaultOptions } = require("expect-puppeteer");
const { webcrypto } = require("crypto");

globalThis.crypto = webcrypto;

// big timeout for external requests to do their thing
setDefaultOptions({ timeout: 60_000 });


