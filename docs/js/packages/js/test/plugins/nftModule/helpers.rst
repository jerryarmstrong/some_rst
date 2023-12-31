packages/js/test/plugins/nftModule/helpers.ts
=============================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import { Test } from 'tape';
import { Metaplex, Nft } from '@/index';

export const assertCollectionHasSize = (
  t: Test,
  collectionNft: Nft,
  expectedSize: number
) => {
  t.equal(
    collectionNft.collectionDetails?.size?.toNumber(),
    expectedSize,
    `collection NFT has the expected size: ${expectedSize}`
  );
};

export const assertRefreshedCollectionHasSize = async (
  t: Test,
  mx: Metaplex,
  collectionNft: Nft,
  expectedSize: number
) => {
  const updateCollectionNft = await mx.nfts().refresh(collectionNft);
  assertCollectionHasSize(t, updateCollectionNft, expectedSize);
};


