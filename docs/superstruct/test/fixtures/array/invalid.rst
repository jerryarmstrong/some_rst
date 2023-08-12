test/fixtures/array/invalid.ts
==============================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { array, number } from '../../..'

export const Struct = array(number())

export const data = 'invalid'

export const error = {
  value: 'invalid',
  type: 'Array<number>',
  path: [],
  branch: [data],
}


