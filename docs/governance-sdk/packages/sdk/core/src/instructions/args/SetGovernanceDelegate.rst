packages/sdk/core/src/instructions/args/SetGovernanceDelegate.ts
================================================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import type { PublicKey } from '@solana/web3.js';

import { InstructionType } from '../InstructionType';

export class SetGovernanceDelegate {
  instruction = InstructionType.SetGovernanceDelegate;
  newGovernanceDelegate?: PublicKey;

  constructor(args: { newGovernanceDelegate?: PublicKey }) {
    this.newGovernanceDelegate = args.newGovernanceDelegate;
  }
}


