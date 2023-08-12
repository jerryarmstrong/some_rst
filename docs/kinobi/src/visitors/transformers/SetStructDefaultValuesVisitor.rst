src/visitors/transformers/SetStructDefaultValuesVisitor.ts
==========================================================

Last edited: 2023-08-04 12:58:33

Contents:

.. code-block:: ts

    import * as nodes from '../../nodes';
import { NodeTransform, TransformNodesVisitor } from './TransformNodesVisitor';

type StructDefaultValueMap = Record<string, Record<string, StructDefaultValue>>;
type StructDefaultValue =
  | (nodes.ValueNode & { strategy?: 'optional' | 'omitted' })
  | null;

export class SetStructDefaultValuesVisitor extends TransformNodesVisitor {
  constructor(readonly map: StructDefaultValueMap) {
    const transforms = Object.entries(map).map(
      ([stack, defaultValues]): NodeTransform => ({
        selector: { kind: 'structTypeNode', stack },
        transformer: (node) => {
          nodes.assertStructTypeNode(node);
          const fields = node.fields.map((field): nodes.StructFieldTypeNode => {
            const defaultValue = defaultValues[field.name];
            if (defaultValue === undefined) return field;
            return nodes.structFieldTypeNode({
              ...field,
              defaultsTo: !defaultValue
                ? null
                : {
                    strategy: defaultValue.strategy ?? 'optional',
                    value: defaultValue,
                  },
            });
          });
          return nodes.structTypeNode(fields);
        },
      })
    );

    super(transforms);
  }
}


