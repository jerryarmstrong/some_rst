test/types/array.ts
===================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { assert, array, number } from '../..'
import { test } from '..'

test<Array<unknown>>((x) => {
  assert(x, array())
  return x
})

test<Array<number>>((x) => {
  assert(x, array(number()))
  return x
})


