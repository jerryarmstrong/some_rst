packages/sdk/core/src/instructions/args/CreateMintGovernance.ts
===============================================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import { Governance } from '../configs/Governance';
import { InstructionType } from '../InstructionType';

export class CreateMintGovernance {
  instruction = InstructionType.CreateMintGovernance;
  /**
   * The configuration for the new Mint Governance
   */
  config: Governance;
  /**
   * Whether or not the mint authority transfer to the new governance
   */
  transferMintAuthorities: boolean;

  constructor(args: { config: Governance; transferMintAuthorities: boolean }) {
    this.config = args.config;
    this.transferMintAuthorities = !!args.transferMintAuthorities;
  }
}


