src/visitors/DefaultVisitor.ts
==============================

Last edited: 2023-08-04 12:58:33

Contents:

.. code-block:: ts

    import * as nodes from '../nodes';
import { BaseThrowVisitor } from './BaseThrowVisitor';
import {
  AutoSetAnchorDiscriminatorsVisitor,
  AutoSetFixedAccountSizesVisitor,
  DeduplicateIdenticalDefinedTypesVisitor,
  DEFAULT_INSTRUCTION_ACCOUNT_DEFAULT_RULES,
  SetInstructionAccountDefaultValuesVisitor,
  TransformU8ArraysToBytesVisitor,
  UnwrapInstructionArgsDefinedTypesVisitor,
  FlattenInstructionArgsStructVisitor,
} from './transformers';
import { visit, Visitor } from './Visitor';

export class DefaultVisitor extends BaseThrowVisitor<nodes.RootNode> {
  visitRoot(currentRoot: nodes.RootNode): nodes.RootNode {
    let root: nodes.Node = currentRoot;
    const updateRoot = (visitor: Visitor<nodes.Node | null>) => {
      const newRoot = visit(root, visitor);
      nodes.assertRootNode(newRoot);
      root = newRoot;
    };

    // Defined types.
    updateRoot(new DeduplicateIdenticalDefinedTypesVisitor());

    // Accounts.
    updateRoot(new AutoSetAnchorDiscriminatorsVisitor());
    updateRoot(new AutoSetFixedAccountSizesVisitor());

    // Instructions.
    updateRoot(
      new SetInstructionAccountDefaultValuesVisitor(
        DEFAULT_INSTRUCTION_ACCOUNT_DEFAULT_RULES
      )
    );
    updateRoot(new UnwrapInstructionArgsDefinedTypesVisitor());
    updateRoot(new FlattenInstructionArgsStructVisitor());

    // Extras.
    updateRoot(new TransformU8ArraysToBytesVisitor());

    return root;
  }
}


