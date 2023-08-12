src/nodes/AccountDataNode.ts
============================

Last edited: 2023-08-04 12:58:33

Contents:

.. code-block:: ts

    import { InvalidKinobiTreeError, mainCase } from '../shared';
import { LinkTypeNode } from './LinkTypeNode';
import type { Node } from './Node';
import { StructTypeNode } from './StructTypeNode';

export type AccountDataNode = {
  readonly __accountDataNode: unique symbol;
  readonly kind: 'accountDataNode';
  readonly name: string;
  readonly struct: StructTypeNode;
  readonly link?: LinkTypeNode;
};

export type AccountDataNodeInput = Omit<
  AccountDataNode,
  '__accountDataNode' | 'kind'
>;

export function accountDataNode(input: AccountDataNodeInput): AccountDataNode {
  if (!input.name) {
    throw new InvalidKinobiTreeError('AccountDataNode must have a name.');
  }
  return {
    kind: 'accountDataNode',
    name: mainCase(input.name),
    struct: input.struct,
    link: input.link,
  } as AccountDataNode;
}

export function isAccountDataNode(node: Node | null): node is AccountDataNode {
  return !!node && node.kind === 'accountDataNode';
}

export function assertAccountDataNode(
  node: Node | null
): asserts node is AccountDataNode {
  if (!isAccountDataNode(node)) {
    throw new Error(`Expected accountDataNode, got ${node?.kind ?? 'null'}.`);
  }
}


