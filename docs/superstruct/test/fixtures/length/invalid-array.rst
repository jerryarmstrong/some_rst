test/fixtures/length/invalid-array.ts
=====================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { array, length, number } from '../../..'

export const Struct = length(array(number()), 1, 5)

export const data = []

export const error = {
  value: [],
  type: 'Array<number> & Length<1,5>',
  path: [],
  branch: [data],
}


