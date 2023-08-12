packages/sdk/core/src/accounts/models/Realm.ts
==============================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import type { PublicKey } from '@solana/web3.js';

import { RealmConfig } from '../../realm/RealmConfig';
import { AccountType } from '../AccountType';

export class Realm {
  accountType = AccountType.RealmV1;
  communityMint: PublicKey;
  config: RealmConfig;
  reserved: Uint8Array;
  votingProposalCount: number;
  authority?: PublicKey;
  name: string;

  constructor(args: {
    communityMint: PublicKey;
    reserved: Uint8Array;
    config: RealmConfig;
    votingProposalCount: number;
    authority?: PublicKey;
    name: string;
  }) {
    this.communityMint = args.communityMint;
    this.config = args.config;
    this.reserved = args.reserved;
    this.votingProposalCount = args.votingProposalCount;
    this.authority = args.authority;
    this.name = args.name;
  }
}


