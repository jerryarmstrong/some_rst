test/fixtures/array/invalid-element.ts
======================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { array, number } from '../../..'

export const Struct = array(number())

export const data = [1, 'invalid', 3]

export const error = {
  value: 'invalid',
  type: 'number',
  path: [1],
  branch: [data, data[1]],
}


