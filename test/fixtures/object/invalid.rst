test/fixtures/object/invalid.ts
===============================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { object, string, number } from '../../..'

export const Struct = object({
  name: string(),
  age: number(),
})

export const data = 'invalid'

export const error = {
  value: 'invalid',
  type: 'Object<{name,age}>',
  path: [],
  branch: [data],
}


