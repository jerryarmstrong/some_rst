test/fixtures/nullable/valid-defined-nested.ts
==============================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { type, string, number, nullable } from '../../..'

export const Struct = type({
  name: nullable(string()),
  age: number(),
})

export const data = {
  name: 'Jill',
  age: 42,
}

export const output = {
  name: 'Jill',
  age: 42,
}


