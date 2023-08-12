test/fixtures/object/invalid-property-unknown.ts
================================================

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
  unknown: true,
}

export const error = {
  value: true,
  type: 'never',
  path: ['unknown'],
  branch: [data, data.unknown],
}


