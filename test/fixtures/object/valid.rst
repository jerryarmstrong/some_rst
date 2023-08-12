test/fixtures/object/valid.ts
=============================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { object, string, number } from '../../..'

export const Struct = object({
  name: string(),
  age: number(),
})

export const data = {
  name: 'john',
  age: 42,
}

export const output = {
  name: 'john',
  age: 42,
}


