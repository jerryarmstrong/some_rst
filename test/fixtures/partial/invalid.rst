test/fixtures/partial/invalid.ts
================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { partial, string, number } from '../../..'

export const Struct = partial({
  name: string(),
  age: number(),
})

export const data = 'invalid'

export const error = {
  value: 'invalid',
  type: 'Partial<{name,age}>',
  path: [],
  branch: [data],
}


