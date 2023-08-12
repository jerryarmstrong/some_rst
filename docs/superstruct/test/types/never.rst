test/types/never.ts
===================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { assert, never } from '../..'
import { test } from '..'

test<never>((x) => {
  assert(x, never())
  return x
})


