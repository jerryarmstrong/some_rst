test/fixtures/map/valid.ts
==========================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { map, string, number } from '../../..'

export const Struct = map(string(), number())

export const data = new Map([
  ['a', 1],
  ['b', 2],
])

export const output = new Map([
  ['a', 1],
  ['b', 2],
])


