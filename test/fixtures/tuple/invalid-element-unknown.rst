test/fixtures/tuple/invalid-element-unknown.ts
==============================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { tuple, string, number } from '../../..'

export const Struct = tuple([string(), number()])

export const data = ['A', 3, 'unknown']

export const error = {
  value: 'unknown',
  type: 'never',
  path: [2],
  branch: [data, data[2]],
}


