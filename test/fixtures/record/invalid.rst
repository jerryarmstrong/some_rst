test/fixtures/record/invalid.ts
===============================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { record, string, number } from '../../..'

export const Struct = record(string(), number())

export const data = 'invalid'

export const error = {
  value: 'invalid',
  type: 'Record<string,number>',
  path: [],
  branch: [data],
}


