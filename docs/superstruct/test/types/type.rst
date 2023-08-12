test/types/type.ts
==================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { assert, type, number } from '../..'
import { test } from '..'

test<{ a: number }>((x) => {
  assert(x, type({ a: number() }))
  return x
})


