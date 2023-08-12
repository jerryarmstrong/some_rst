src/visitors/transformers/FlattenInstructionArgsStructVisitor.ts
================================================================

Last edited: 2023-08-04 12:58:33

Contents:

.. code-block:: ts

    import * as nodes from '../../nodes';
import { TransformNodesVisitor } from './TransformNodesVisitor';
import { flattenStruct } from './FlattenStructVisitor';

export class FlattenInstructionArgsStructVisitor extends TransformNodesVisitor {
  constructor() {
    super([
      {
        selector: { kind: 'instructionNode' },
        transformer: (instruction) => {
          nodes.assertInstructionNode(instruction);
          return nodes.instructionNode({
            ...instruction,
            dataArgs: nodes.instructionDataArgsNode({
              ...instruction.dataArgs,
              struct: flattenStruct(instruction.dataArgs.struct),
            }),
          });
        },
      },
    ]);
  }
}


