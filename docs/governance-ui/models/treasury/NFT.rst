models/treasury/NFT.ts
======================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    export interface NFT {
  address: string
  collection?: null | {
    address: string
    name: string
    nftCount?: number
    image: string
  }
  image: string
  name: string
  owner: {
    address: string
  }
}


