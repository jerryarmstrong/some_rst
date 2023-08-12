src/visitors/transformers/DeleteNodesVisitor.ts
===============================================

Last edited: 2023-08-04 12:58:33

Contents:

.. code-block:: ts

    import { NodeSelector } from '../NodeSelector';
import { TransformNodesVisitor } from './TransformNodesVisitor';

export class DeleteNodesVisitor extends TransformNodesVisitor {
  constructor(selectors: NodeSelector[]) {
    super(
      selectors.map((selector) => ({
        selector,
        transformer: () => null,
      }))
    );
  }
}


