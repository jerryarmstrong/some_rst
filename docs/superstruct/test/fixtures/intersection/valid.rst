test/fixtures/intersection/valid.ts
===================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { type, intersection, string, number } from '../../..'

const A = type({ a: string() })
const B = type({ b: number() })

export const Struct = intersection([A, B])

export const data = {
  a: 'a',
  b: 42,
}

export const output = {
  a: 'a',
  b: 42,
}


