hooks/useTreasuryInfo/groupNftsByWallet.ts
==========================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import { NFT } from '@models/treasury/NFT'

export function groupNftsByWallet(nfts: NFT[]) {
  return nfts.reduce((acc, nft) => {
    if (!acc[nft.owner.address]) {
      acc[nft.owner.address] = []
    }

    acc[nft.owner.address].push(nft)

    return acc
  }, {} as { [wallet: string]: NFT[] })
}


