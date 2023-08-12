test/types/any.ts
=================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { assert, any } from '../..'
import { test } from '..'

test<any>((x) => {
  assert(x, any())
  return x
})


