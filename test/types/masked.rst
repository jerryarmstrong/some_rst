test/types/masked.ts
====================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { assert, masked, object, number } from '../..'
import { test } from '..'

test<{ a: number }>((x) => {
  assert(x, masked(object({ a: number() })))
  return x
})


