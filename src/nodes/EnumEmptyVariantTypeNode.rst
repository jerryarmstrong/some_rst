src/nodes/EnumEmptyVariantTypeNode.ts
=====================================

Last edited: 2023-08-04 12:58:33

Contents:

.. code-block:: ts

    import type { IdlTypeEnumVariant } from '../idl';
import { InvalidKinobiTreeError, mainCase } from '../shared';
import type { Node } from './Node';

export type EnumEmptyVariantTypeNode = {
  readonly __enumEmptyVariantTypeNode: unique symbol;
  readonly kind: 'enumEmptyVariantTypeNode';
  readonly name: string;
};

export function enumEmptyVariantTypeNode(
  name: string
): EnumEmptyVariantTypeNode {
  if (!name) {
    throw new InvalidKinobiTreeError(
      'EnumEmptyVariantTypeNode must have a name.'
    );
  }
  return {
    kind: 'enumEmptyVariantTypeNode',
    name: mainCase(name),
  } as EnumEmptyVariantTypeNode;
}

export function enumEmptyVariantTypeNodeFromIdl(
  idl: IdlTypeEnumVariant
): EnumEmptyVariantTypeNode {
  return enumEmptyVariantTypeNode(idl.name ?? '');
}

export function isEnumEmptyVariantTypeNode(
  node: Node | null
): node is EnumEmptyVariantTypeNode {
  return !!node && node.kind === 'enumEmptyVariantTypeNode';
}

export function assertEnumEmptyVariantTypeNode(
  node: Node | null
): asserts node is EnumEmptyVariantTypeNode {
  if (!isEnumEmptyVariantTypeNode(node)) {
    throw new Error(
      `Expected enumEmptyVariantTypeNode, got ${node?.kind ?? 'null'}.`
    );
  }
}


