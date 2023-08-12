test/fixtures/type/invalid.ts
=============================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { type, string, number } from '../../..'

export const Struct = type({
  name: string(),
  age: number(),
})

export const data = 'invalid'

export const error = {
  value: 'invalid',
  type: 'Type<{name,age}>',
  path: [],
  branch: [data],
}


