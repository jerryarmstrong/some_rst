test/fixtures/record/invalid-property.ts
========================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { record, string, number } from '../../..'

export const Struct = record(string(), number())

export const data = {
  a: 'a',
  b: 'b',
}

export const error = {
  value: 'a',
  type: 'number',
  path: ['a'],
  branch: [data, data.a],
}


