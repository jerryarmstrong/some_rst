test/fixtures/set/invalid-element.ts
====================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { set, number } from '../../..'

export const Struct = set(number())

export const data = new Set([1, 'b', 3])

export const error = {
  value: new Set([1, 'b', 3]),
  type: 'Set<number>',
  path: [],
  branch: [data],
}


