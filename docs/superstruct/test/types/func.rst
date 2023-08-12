test/types/func.ts
==================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { assert, func } from '../..'
import { test } from '..'

test<Function>((x) => {
  assert(x, func())
  return x
})


