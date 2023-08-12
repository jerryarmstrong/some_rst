test/fixtures/set/invalid.ts
============================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { set, number } from '../../..'

export const Struct = set(number())

export const data = 'invalid'

export const error = {
  value: 'invalid',
  type: 'Set<number>',
  path: [],
  branch: [data],
}


