packages/sdk/core/src/instructions/args/AddSignatory.ts
=======================================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import type { PublicKey } from '@solana/web3.js';

import { InstructionType } from '../InstructionType';

export class AddSignatory {
  instruction = InstructionType.AddSignatory;
  /**
   * Public key of the signatory
   */
  signatory: PublicKey;

  constructor(args: { signatory: PublicKey }) {
    this.signatory = args.signatory;
  }
}


