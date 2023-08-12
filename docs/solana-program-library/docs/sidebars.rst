docs/sidebars.js
================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: js

    module.exports = {
  docs: [
    "introduction",
    "token",
    "token-swap",
    "token-lending",
    "associated-token-account",
    "memo",
    "name-service",
    "shared-memory",
    {
      type: 'category',
      label: 'Stake Pool',
      collapsed: true,
      items: [
        "stake-pool",
        "stake-pool/quickstart",
        "stake-pool/overview",
        "stake-pool/cli",
      ],
    },
    "feature-proposal",
  ],
};


