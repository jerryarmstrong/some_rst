packages/gumdrop/src/models/account.ts
======================================

Last edited: 2022-08-25 19:21:42

Contents:

.. code-block:: ts

    import { AccountInfo } from '@solana/web3.js';

import { AccountInfo as TokenAccountInfo } from '@solana/spl-token';

export interface TokenAccount {
  pubkey: string;
  account: AccountInfo<Buffer>;
  info: TokenAccountInfo;
}


