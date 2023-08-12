src/lib/scalars/BigNumber.ts
============================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { BigNumber } from 'bignumber.js';
import { Kind, ValueNode, GraphQLScalarType } from 'graphql';

export const BigNumberScalar = new GraphQLScalarType({
  name: 'BigNumber',
  description: 'A potentially large number value. Compatible with `BigNumber.js`',
  parseLiteral: (ast: ValueNode): BigNumber =>
    // @ts-ignore
    ast.kind === Kind.STRING ? new BigNumber(ast.value) : null,
  // @ts-ignore
  parseValue: (value: string): BigNumber => new BigNumber(value),
  // @ts-ignore
  serialize: (value: BigNumber): string => value.toString(),
})


