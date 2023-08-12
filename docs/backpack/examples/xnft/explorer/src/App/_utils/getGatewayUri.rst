examples/xnft/explorer/src/App/_utils/getGatewayUri.ts
======================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    const gatewayUri = (uri: string): string =>
  uri.replace("ipfs://", "https://nftstorage.link/ipfs/");

export default gatewayUri;


