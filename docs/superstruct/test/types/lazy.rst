test/types/lazy.ts
==================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { assert, lazy, string } from '../..'
import { test } from '..'

test<string>((x) => {
  assert(
    x,
    lazy(() => string())
  )
  return x
})


