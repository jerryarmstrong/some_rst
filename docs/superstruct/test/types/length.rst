test/types/length.ts
====================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { assert, length, string, array } from '../..'
import { test } from '..'

test<string>((x) => {
  assert(x, length(string(), 1, 5))
  return x
})

test<Array<unknown>>((x) => {
  assert(x, length(array(), 1, 5))
  return x
})


