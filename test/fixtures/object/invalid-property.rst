test/fixtures/object/invalid-property.ts
========================================

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
  age: 'invalid',
}

export const error = {
  value: 'invalid',
  type: 'number',
  path: ['age'],
  branch: [data, data.age],
}


