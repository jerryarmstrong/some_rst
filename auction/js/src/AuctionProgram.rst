auction/js/src/AuctionProgram.ts
================================

Last edited: 2022-10-11 23:41:10

Contents:

.. code-block:: ts

    import { PublicKey } from '@solana/web3.js';
import { config, Program } from '@metaplex-foundation/mpl-core';

export class AuctionProgram extends Program {
  static readonly PREFIX = 'auction';
  static readonly EXTENDED = 'extended';
  static readonly PUBKEY = new PublicKey(config.programs.auction);
}


