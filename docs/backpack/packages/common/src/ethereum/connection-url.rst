packages/common/src/ethereum/connection-url.ts
==============================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    export const EthereumConnectionUrl = {
  MAINNET: `https://swr.xnfts.dev/ethereum-rpc-proxy`,
  GOERLI:
    "https://eth-goerli.g.alchemy.com/v2/6QnM1O0pB17Qo47Cw9qMipDGWX7xAVWc",
  LOCALNET: "http://localhost:8545",

  DEFAULT:
    process.env.DEFAULT_ETHEREUM_CONNECTION_URL ||
    "https://swr.xnfts.dev/ethereum-rpc-proxy",
};

export const EthereumChainIds = {
  "0x1": "MAINNET",
  "0x5": "GOERLI",
};


