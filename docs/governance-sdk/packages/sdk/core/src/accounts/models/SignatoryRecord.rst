packages/sdk/core/src/accounts/models/SignatoryRecord.ts
========================================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import type { PublicKey } from '@solana/web3.js';

import { AccountType } from '../AccountType';

export class SignatoryRecord {
  accountType = AccountType.SignatoryRecordV1;
  proposal: PublicKey;
  signatory: PublicKey;
  signedOff: boolean;

  constructor(args: { proposal: PublicKey; signatory: PublicKey; signedOff: boolean }) {
    this.proposal = args.proposal;
    this.signatory = args.signatory;
    this.signedOff = args.signedOff;
  }
}


