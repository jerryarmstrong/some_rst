js/packages/common/src/contexts/accounts/types.ts
=================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import { AccountInfo } from '@solana/web3.js';
import { StringPublicKey } from '../../utils';

export interface ParsedAccountBase {
  pubkey: StringPublicKey;
  account: AccountInfo<Buffer>;
  info: any; // TODO: change to unknown
}

export type AccountParser = (
  pubkey: StringPublicKey,
  data: AccountInfo<Buffer>,
) => ParsedAccountBase | undefined;

export interface ParsedAccount<T> extends ParsedAccountBase {
  info: T;
}


