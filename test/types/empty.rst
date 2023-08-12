test/types/empty.ts
===================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { assert, empty, string, array } from '../..'
import { test } from '..'

test<string>((x) => {
  assert(x, empty(string()))
  return x
})

test<Array<unknown>>((x) => {
  assert(x, empty(array()))
  return x
})


