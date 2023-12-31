packages/sdk/core/src/instructions/args/InsertTransaction.ts
============================================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import type { InstructionData } from '../InstructionData';
import { InstructionType } from '../InstructionType';

export class InsertTransaction {
  instruction = InstructionType.InsertTransaction;
  index: number;
  optionIndex: number;
  holdUpTime: number;

  // V1
  instructionData?: InstructionData;

  // V2
  instructions?: InstructionData[];

  constructor(args: {
    index: number;
    optionIndex: number;
    holdUpTime: number;

    // V1
    instructionData?: InstructionData;

    // V2
    instructions?: InstructionData[];
  }) {
    this.index = args.index;
    this.optionIndex = args.optionIndex;
    this.holdUpTime = args.holdUpTime;
    // V1
    this.instructionData = args.instructionData;
    // V2
    this.instructions = args.instructions;
  }
}


