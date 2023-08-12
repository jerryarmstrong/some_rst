src/nodes/BytesTypeNode.ts
==========================

Last edited: 2023-08-04 12:58:33

Contents:

.. code-block:: ts

    import {
  SizeStrategy,
  displaySizeStrategy,
  remainderSize,
} from '../shared/SizeStrategy';
import type { Node } from './Node';

export type BytesTypeNode = {
  readonly __bytesTypeNode: unique symbol;
  readonly kind: 'bytesTypeNode';
  readonly size: SizeStrategy;
};

export function bytesTypeNode(size?: SizeStrategy): BytesTypeNode {
  return {
    kind: 'bytesTypeNode',
    size: size ?? remainderSize(),
  } as BytesTypeNode;
}

export function displayBytesTypeNode(node: BytesTypeNode): string {
  return `bytes(${displaySizeStrategy(node.size)})`;
}

export function isBytesTypeNode(node: Node | null): node is BytesTypeNode {
  return !!node && node.kind === 'bytesTypeNode';
}

export function assertBytesTypeNode(
  node: Node | null
): asserts node is BytesTypeNode {
  if (!isBytesTypeNode(node)) {
    throw new Error(`Expected bytesTypeNode, got ${node?.kind ?? 'null'}.`);
  }
}


