packages/sdk/core/src/instructions/InstructionData.ts
=====================================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import type { PublicKey } from '@solana/web3.js';

import type { AccountMetaData } from '../accounts/AccountMetaData';

export class InstructionData {
  programId: PublicKey;
  accounts: AccountMetaData[];
  data: Uint8Array;

  constructor(args: { programId: PublicKey; accounts: AccountMetaData[]; data: Uint8Array }) {
    this.programId = args.programId;
    this.accounts = args.accounts;
    this.data = args.data;
  }
}


