test/types/tuple.ts
===================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { assert, tuple, string, number } from '../..'
import { test } from '..'

test<[string, number]>((x) => {
  assert(x, tuple([string(), number()]))
  return x
})


