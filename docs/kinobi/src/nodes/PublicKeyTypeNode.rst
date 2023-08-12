src/nodes/PublicKeyTypeNode.ts
==============================

Last edited: 2023-08-04 12:58:33

Contents:

.. code-block:: ts

    import type { Node } from './Node';

export type PublicKeyTypeNode = {
  readonly __publicKeyTypeNode: unique symbol;
  readonly kind: 'publicKeyTypeNode';
};

export function publicKeyTypeNode(): PublicKeyTypeNode {
  return { kind: 'publicKeyTypeNode' } as PublicKeyTypeNode;
}

export function isPublicKeyTypeNode(
  node: Node | null
): node is PublicKeyTypeNode {
  return !!node && node.kind === 'publicKeyTypeNode';
}

export function assertPublicKeyTypeNode(
  node: Node | null
): asserts node is PublicKeyTypeNode {
  if (!isPublicKeyTypeNode(node)) {
    throw new Error(`Expected publicKeyTypeNode, got ${node?.kind ?? 'null'}.`);
  }
}


