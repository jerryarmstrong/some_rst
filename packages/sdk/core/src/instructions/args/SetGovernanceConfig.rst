packages/sdk/core/src/instructions/args/SetGovernanceConfig.ts
==============================================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import { Governance } from '../configs/Governance';
import { InstructionType } from '../InstructionType';

export class SetGovernanceConfig {
  instruction = InstructionType.SetGovernanceConfig;
  config: Governance;

  constructor(args: { config: Governance }) {
    this.config = args.config;
  }
}


