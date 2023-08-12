test/fixtures/optional/valid-undefined-nested.ts
================================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { type, string, number, optional } from '../../..'

export const Struct = type({
  name: optional(string()),
  age: number(),
})

export const data = {
  age: 42,
}

export const output = {
  age: 42,
}


