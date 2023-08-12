test/fixtures/type/valid.ts
===========================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { type, string, number } from '../../..'

export const Struct = type({
  name: string(),
  age: number(),
})

export const data = {
  name: 'john',
  age: 42,
}

export const output = data


