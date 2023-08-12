test/fixtures/array/invalid-opaque.ts
=====================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { array } from '../../..'

export const Struct = array()

export const data = 'invalid'

export const error = {
  value: 'invalid',
  type: 'Array<unknown>',
  path: [],
  branch: [data],
}


