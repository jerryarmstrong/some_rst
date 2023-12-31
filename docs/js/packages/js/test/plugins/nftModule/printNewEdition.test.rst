packages/js/test/plugins/nftModule/printNewEdition.test.ts
==========================================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import test, { Test } from 'tape';
import spok, { Specifications } from 'spok';
import {
  assertThrows,
  createNft,
  killStuckProcess,
  metaplex,
  spokSameBignum,
  spokSamePubkey,
} from '../../helpers';
import { Nft, toBigNumber } from '@/index';
import { assertNftOriginalEdition } from '@/plugins';

killStuckProcess();

test('[nftModule] it can print a new edition from an original edition', async (t: Test) => {
  // Given an existing Original NFT.
  const mx = await metaplex();
  const originalNft = await createNft(mx, {
    name: 'Original Nft On-Chain Name',
    maxSupply: toBigNumber(100),
    json: {
      name: 'Original Nft Name',
      description: 'Original Nft Description',
    },
  });

  // When we print a new edition of the NFT.
  const {
    nft: printNft,
    updatedSupply,
    tokenAddress,
  } = await mx.nfts().printNewEdition({ originalMint: originalNft.address });

  // Then we created and returned the printed NFT with the right data.
  const expectedNft = {
    model: 'nft',
    name: 'Original Nft On-Chain Name',
    json: {
      name: 'Original Nft Name',
      description: 'Original Nft Description',
    },
    edition: {
      isOriginal: false,
      parent: spokSamePubkey(originalNft.edition.address),
      number: spokSameBignum(1),
    },
    token: {
      address: spokSamePubkey(tokenAddress),
      isAssociatedToken: true,
    },
  } as unknown as Specifications<Nft>;
  spok(t, printNft, { $topic: 'nft', ...expectedNft });

  // And the data was stored in the blockchain.
  const retrievedNft = await mx.nfts().refresh(printNft);
  spok(t, retrievedNft, { $topic: 'Retrieved Nft', ...expectedNft });

  // And the original NFT edition was updated.
  t.equals(updatedSupply.toNumber(), 1);
});

test('[nftModule] it keeps track of the edition number', async (t: Test) => {
  // Given an existing Original NFT.
  const mx = await metaplex();
  const originalNft = await createNft(mx, { maxSupply: toBigNumber(100) });

  // When we print 3 new editions of the NFT.
  const input = { originalMint: originalNft.address };
  const { nft: printNft1 } = await mx.nfts().printNewEdition(input);
  const { nft: printNft2 } = await mx.nfts().printNewEdition(input);
  const { nft: printNft3 } = await mx.nfts().printNewEdition(input);

  // Then each edition knows their number and are associated with the same parent.
  isPrintOfOriginal(t, printNft1, originalNft, 1);
  isPrintOfOriginal(t, printNft2, originalNft, 2);
  isPrintOfOriginal(t, printNft3, originalNft, 3);
});

test('[nftModule] it can print unlimited editions', async (t: Test) => {
  // Given an existing Original NFT with unlimited supply.
  const mx = await metaplex();
  const originalNft = await createNft(mx, { maxSupply: null });
  const originalEdition = originalNft.edition;
  assertNftOriginalEdition(originalEdition);
  t.equals(originalEdition.maxSupply, null);

  // When we print an edition of the NFT.
  const { nft: printNft } = await mx
    .nfts()
    .printNewEdition({ originalMint: originalNft.address });

  // Then we successfully printed the first NFT of an unlimited collection.
  isPrintOfOriginal(t, printNft, originalNft, 1);
});

test('[nftModule] it cannot print when the maxSupply is zero', async (t: Test) => {
  // Given an existing Original NFT with a maxSupply of zero.
  const mx = await metaplex();
  const originalNft = await createNft(mx, { maxSupply: toBigNumber(0) });

  // When we try to print an edition of the NFT.
  const promise = mx
    .nfts()
    .printNewEdition({ originalMint: originalNft.address });

  // Then we should get an error.
  await assertThrows(t, promise, /Edition Number greater than max supply/);
});

const isPrintOfOriginal = (
  t: Test,
  print: Nft,
  original: Nft,
  edition: number
) => {
  spok(t, print, {
    $topic: 'print NFT #' + edition,
    edition: {
      parent: spokSamePubkey(original.edition.address),
      number: spokSameBignum(edition),
    },
  } as unknown as Specifications<Nft>);
};


