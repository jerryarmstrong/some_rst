test/fixtures/partial/invalid-property.ts
=========================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { partial, string, number } from '../../..'

export const Struct = partial({
  name: string(),
  age: number(),
})

export const data = {
  age: 'invalid',
}

export const error = {
  value: 'invalid',
  type: 'number',
  path: ['age'],
  branch: [data, data.age],
}


