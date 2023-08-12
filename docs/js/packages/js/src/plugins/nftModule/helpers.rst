packages/js/src/plugins/nftModule/helpers.ts
============================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import type { PublicKey } from '@solana/web3.js';
import type { Nft, NftWithToken, Sft, SftWithToken } from './models';
import type { Metadata } from './models/Metadata';
import { PublicKeyValues, toPublicKey } from '@/types';

export type HasMintAddress =
  | Nft
  | Sft
  | NftWithToken
  | SftWithToken
  | Metadata
  | PublicKey;

export const toMintAddress = (
  value: PublicKeyValues | HasMintAddress
): PublicKey => {
  return typeof value === 'object' && 'mintAddress' in value
    ? value.mintAddress
    : toPublicKey(value);
};


