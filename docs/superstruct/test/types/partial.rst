test/types/partial.ts
=====================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { assert, object, number } from '../..'
import { test } from '..'

test<{ a?: number }>((x) => {
  assert(x, object({ a: number() }))
  return x
})


