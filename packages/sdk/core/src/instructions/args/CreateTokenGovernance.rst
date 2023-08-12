packages/sdk/core/src/instructions/args/CreateTokenGovernance.ts
================================================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import { Governance } from '../configs/Governance';
import { InstructionType } from '../InstructionType';

export class CreateTokenGovernance {
  instruction = InstructionType.CreateTokenGovernance;
  config: Governance;
  transferTokenOwner: boolean;

  constructor(args: { config: Governance; transferTokenOwner: boolean }) {
    this.config = args.config;
    this.transferTokenOwner = !!args.transferTokenOwner;
  }
}


