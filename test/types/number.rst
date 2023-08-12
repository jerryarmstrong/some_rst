test/types/number.ts
====================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { assert, number } from '../..'
import { test } from '..'

test<number>((x) => {
  assert(x, number())
  return x
})


