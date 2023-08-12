test/fixtures/map/invalid.ts
============================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { map, string, number } from '../../..'

export const Struct = map(string(), number())

export const data = 'invalid'

export const error = {
  value: 'invalid',
  type: 'Map<string,number>',
  path: [],
  branch: [data],
}


