test/fixtures/tuple/invalid-element-missing.ts
==============================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { tuple, string, number } from '../../..'

export const Struct = tuple([string(), number()])

export const data = ['A']

export const error = {
  value: undefined,
  type: 'number',
  path: [1],
  branch: [data, data[1]],
}


