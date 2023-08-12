cNft-Governance/governance-program-library/migrations/deploy.ts
===============================================================

Last edited: 2023-07-14 15:51:14

Contents:

.. code-block:: ts

    // Migrations are an early feature. Currently, they're nothing more than this
// single deploy script that's invoked from the CLI, injecting a provider
// configured from the workspace's Anchor.toml.

const anchor = require("@project-serum/anchor");

module.exports = async function (provider) {
  // Configure client to use the provider.
  anchor.setProvider(provider);

  // Add your deploy script here.
};


