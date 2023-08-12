test/types/struct.ts
====================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { assert, struct } from '../..'
import { test } from '..'

test<string>((x) => {
  assert(
    x,
    struct<string>('custom', () => true)
  )
  return x
})


