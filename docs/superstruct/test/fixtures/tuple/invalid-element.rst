test/fixtures/tuple/invalid-element.ts
======================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { tuple, string, number } from '../../..'

export const Struct = tuple([string(), number()])

export const data = [false, 3]

export const error = {
  value: false,
  type: 'string',
  path: [0],
  branch: [data, data[0]],
}


