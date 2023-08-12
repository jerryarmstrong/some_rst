src/lib/scalars/Cursor.ts
=========================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Kind, ValueNode, GraphQLScalarType } from 'graphql';

export const CursorScalar = new GraphQLScalarType({
  name: 'Cursor',
  description: 'An opaque string used for pagination',
  // @ts-ignore
  parseLiteral: (ast: ValueNode): string => (ast.kind === Kind.STRING ? ast.value : null),
  // @ts-ignore
  parseValue: (value: string): string => value,
  // @ts-ignore
  serialize: (value: string): string => value,
});


