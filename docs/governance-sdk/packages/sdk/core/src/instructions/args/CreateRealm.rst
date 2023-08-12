packages/sdk/core/src/instructions/args/CreateRealm.ts
======================================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import { Realm } from '../configs/Realm';
import { InstructionType } from '../InstructionType';

export class CreateRealm {
  instruction = InstructionType.CreateRealm;
  configArgs: Realm;
  name: string;

  constructor(args: { name: string; configArgs: Realm }) {
    this.name = args.name;
    this.configArgs = args.configArgs;
  }
}


