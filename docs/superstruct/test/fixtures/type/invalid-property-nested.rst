test/fixtures/type/invalid-property-nested.ts
=============================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { type, string, number } from '../../..'

export const Struct = type({
  id: number(),
  person: type({
    name: string(),
    age: number(),
  }),
})

export const data = {
  id: 1,
}

export const error = {
  value: undefined,
  type: 'Type<{name,age}>',
  path: ['person'],
  branch: [data, undefined],
}


