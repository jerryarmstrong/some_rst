packages/app-mobile/src/types/types.ts
======================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import type { NftCollection } from "@coral-xyz/common";
import type { useBlockchainTokensSorted } from "@coral-xyz/recoil";
export type Token = ReturnType<typeof useBlockchainTokensSorted>[number];
export type { Wallet } from "@coral-xyz/recoil";

export type NavTokenOptions = any;
export type PublicKey = string;

export type NftCollectionsWithId = {
  publicKey: string;
  collections: NftCollection[];
};

export type SingleNftData = {
  title: string;
  nftId: string;
  publicKey: string;
  connectionUrl: string;
};

export type CollectionNftData = {
  title: string;
  collectionId: string;
  publicKey: string;
  connectionUrl: string;
};


