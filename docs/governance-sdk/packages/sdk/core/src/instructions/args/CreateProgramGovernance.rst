packages/sdk/core/src/instructions/args/CreateProgramGovernance.ts
==================================================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import { Governance } from '../configs/Governance';
import { InstructionType } from '../InstructionType';

export class CreateProgramGovernance {
  instruction = InstructionType.CreateProgramGovernance;
  /**
   * The configuration for the new Program Governance
   */
  config: Governance;
  /**
   * Whether the the authority to upgrade the program is transfered to this
   * governance
   */
  transferUpgradeAuthority: boolean;

  constructor(args: { config: Governance; transferUpgradeAuthority: boolean }) {
    this.config = args.config;
    this.transferUpgradeAuthority = !!args.transferUpgradeAuthority;
  }
}


