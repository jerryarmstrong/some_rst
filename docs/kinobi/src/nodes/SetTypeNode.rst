src/nodes/SetTypeNode.ts
========================

Last edited: 2023-08-04 12:58:33

Contents:

.. code-block:: ts

    import type { IdlTypeSet } from '../idl';
import {
  SizeStrategy,
  fixedSize,
  prefixedSize,
  remainderSize,
} from '../shared';
import type { Node } from './Node';
import { numberTypeNode } from './NumberTypeNode';
import { TypeNode, createTypeNodeFromIdl } from './TypeNode';

export type SetTypeNode = {
  readonly __setTypeNode: unique symbol;
  readonly kind: 'setTypeNode';
  readonly child: TypeNode;
  readonly size: SizeStrategy;
  readonly idlSet: 'hashSet' | 'bTreeSet';
};

export function setTypeNode(
  child: TypeNode,
  options: {
    readonly size?: SizeStrategy;
    readonly idlSet?: SetTypeNode['idlSet'];
  } = {}
): SetTypeNode {
  return {
    kind: 'setTypeNode',
    child,
    size: options.size ?? prefixedSize(),
    idlSet: options.idlSet ?? 'hashSet',
  } as SetTypeNode;
}

export function setTypeNodeFromIdl(idl: IdlTypeSet): SetTypeNode {
  const child = 'hashSet' in idl ? idl.hashSet : idl.bTreeSet;
  let size: SetTypeNode['size'] | undefined;
  if (idl.size === 'remainder') {
    size = remainderSize();
  } else if (typeof idl.size === 'number') {
    size = fixedSize(idl.size);
  } else if (idl.size) {
    size = prefixedSize(numberTypeNode(idl.size));
  }
  return setTypeNode(createTypeNodeFromIdl(child), {
    size,
    idlSet: 'hashSet' in idl ? 'hashSet' : 'bTreeSet',
  });
}

export function isSetTypeNode(node: Node | null): node is SetTypeNode {
  return !!node && node.kind === 'setTypeNode';
}

export function assertSetTypeNode(
  node: Node | null
): asserts node is SetTypeNode {
  if (!isSetTypeNode(node)) {
    throw new Error(`Expected setTypeNode, got ${node?.kind ?? 'null'}.`);
  }
}


