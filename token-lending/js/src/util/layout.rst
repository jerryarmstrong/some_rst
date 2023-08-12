token-lending/js/src/util/layout.ts
===================================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: ts

    import { AccountInfo, PublicKey } from '@solana/web3.js';

export type Parser<T> = (
    pubkey: PublicKey,
    info: AccountInfo<Uint8Array>
) =>
    | {
          pubkey: PublicKey;
          info: AccountInfo<Uint8Array>;
          data: T;
      }
    | undefined;


