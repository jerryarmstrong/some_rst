src/models/account.ts
=====================

Last edited: 2020-11-17 14:49:57

Contents:

.. code-block:: ts

    import { AccountInfo, PublicKey } from "@solana/web3.js";

import { AccountInfo as TokenAccountInfo } from "@solana/spl-token";

export interface TokenAccount {
  pubkey: PublicKey;
  account: AccountInfo<Buffer>;
  info: TokenAccountInfo;
}


