test/fixtures/tuple/invalid.ts
==============================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { tuple, string, number } from '../../..'

export const Struct = tuple([string(), number()])

export const data = 'invalid'

export const error = {
  value: 'invalid',
  type: '[string,number]',
  path: [],
  branch: [data],
}


