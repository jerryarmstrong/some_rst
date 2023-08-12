test/fixtures/partial/invalid-property-unknown.ts
=================================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { partial, string, number } from '../../..'

export const Struct = partial({
  name: string(),
  age: number(),
})

export const data = {
  name: 'john',
  unknown: true,
}

export const error = {
  value: true,
  type: 'never',
  path: ['unknown'],
  branch: [data, data.unknown],
}


