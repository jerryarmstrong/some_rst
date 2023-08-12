src/nodes/EnumTupleVariantTypeNode.ts
=====================================

Last edited: 2023-08-04 12:58:33

Contents:

.. code-block:: ts

    import type { IdlType, IdlTypeEnumVariant } from '../idl';
import { InvalidKinobiTreeError, mainCase } from '../shared';
import type { Node } from './Node';
import { TupleTypeNode, tupleTypeNodeFromIdl } from './TupleTypeNode';

export type EnumTupleVariantTypeNode = {
  readonly __enumTupleVariantTypeNode: unique symbol;
  readonly kind: 'enumTupleVariantTypeNode';
  readonly name: string;
  readonly tuple: TupleTypeNode;
};

export function enumTupleVariantTypeNode(
  name: string,
  tuple: TupleTypeNode
): EnumTupleVariantTypeNode {
  if (!name) {
    throw new InvalidKinobiTreeError(
      'EnumTupleVariantTypeNode must have a name.'
    );
  }
  return {
    kind: 'enumTupleVariantTypeNode',
    name: mainCase(name),
    tuple,
  } as EnumTupleVariantTypeNode;
}

export function enumTupleVariantTypeNodeFromIdl(
  idl: IdlTypeEnumVariant
): EnumTupleVariantTypeNode {
  const name = idl.name ?? '';
  return enumTupleVariantTypeNode(
    name,
    tupleTypeNodeFromIdl({ tuple: idl.fields as IdlType[] })
  );
}

export function isEnumTupleVariantTypeNode(
  node: Node | null
): node is EnumTupleVariantTypeNode {
  return !!node && node.kind === 'enumTupleVariantTypeNode';
}

export function assertEnumTupleVariantTypeNode(
  node: Node | null
): asserts node is EnumTupleVariantTypeNode {
  if (!isEnumTupleVariantTypeNode(node)) {
    throw new Error(
      `Expected enumTupleVariantTypeNode, got ${node?.kind ?? 'null'}.`
    );
  }
}


