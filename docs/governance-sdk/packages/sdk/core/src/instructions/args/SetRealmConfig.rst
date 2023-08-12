packages/sdk/core/src/instructions/args/SetRealmConfig.ts
=========================================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import type { Realm } from '../configs/Realm';
import { InstructionType } from '../InstructionType';

export class SetRealmConfig {
  instruction = InstructionType.SetRealmConfig;
  configArgs: Realm;

  constructor(args: { configArgs: Realm }) {
    this.configArgs = args.configArgs;
  }
}


