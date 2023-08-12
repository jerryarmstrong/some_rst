src/visitors/transformers/AutoSetFixedAccountSizesVisitor.ts
============================================================

Last edited: 2023-08-04 12:58:33

Contents:

.. code-block:: ts

    import * as nodes from '../../nodes';
import { GetByteSizeVisitor } from '../aggregators';
import { BaseThrowVisitor } from '../BaseThrowVisitor';
import { visit } from '../Visitor';
import { TransformNodesVisitor } from './TransformNodesVisitor';

export class AutoSetFixedAccountSizesVisitor extends BaseThrowVisitor<nodes.RootNode> {
  visitRoot(root: nodes.RootNode): nodes.RootNode {
    // Prepare the visitor that gets the byte size of a type.
    const byteSizeVisitor = new GetByteSizeVisitor();
    byteSizeVisitor.registerDefinedTypes(nodes.getAllDefinedTypes(root));

    // Prepare the visitor that transforms account nodes.
    const transformVisitor = new TransformNodesVisitor([
      {
        selector: (node) =>
          nodes.isAccountNode(node) && node.size === undefined,
        transformer: (node) => {
          nodes.assertAccountNode(node);
          const size = visit(node.data, byteSizeVisitor);
          if (size === null) return node;
          return nodes.accountNode({ ...node, size });
        },
      },
    ]);

    // Execute the transform visitor on the Root node.
    const transformedRoot = visit(root, transformVisitor);
    nodes.assertRootNode(transformedRoot);
    return transformedRoot;
  }
}


