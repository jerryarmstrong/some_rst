test/fixtures/union/invalid.ts
==============================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { type, union, string, number } from '../../..'

const A = type({ a: string() })
const B = type({ b: number() })

export const Struct = union([A, B])

export const data = {
  b: 'invalid',
}

export const error = {
  type: 'Type<{a}> | Type<{b}>',
  value: { b: 'invalid' },
  path: [],
  branch: [data],
}


