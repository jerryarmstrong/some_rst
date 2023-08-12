constants/endpoints.ts
======================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    export const MAINNET_RPC =
  process.env.NEXT_PUBLIC_MAINNET_RPC ||
  process.env.MAINNET_RPC ||
  'http://realms-realms-c335.mainnet.rpcpool.com/258d3727-bb96-409d-abea-0b1b4c48af29/'

export const DEVNET_RPC =
  process.env.NEXT_PUBLIC_DEVNET_RPC ||
  process.env.DEVNET_RPC ||
  'https://mango.devnet.rpcpool.com'


