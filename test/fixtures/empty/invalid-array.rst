test/fixtures/empty/invalid-array.ts
====================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { array, empty } from '../../..'

export const Struct = empty(array())

export const data = ['invalid']

export const error = {
  value: ['invalid'],
  type: 'Array<unknown> & Empty',
  path: [],
  branch: [data],
}


