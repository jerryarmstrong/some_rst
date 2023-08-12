test/types/pattern.ts
=====================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { assert, pattern, string } from '../..'
import { test } from '..'

test<string>((x) => {
  assert(x, pattern(string(), /.*/))
  return x
})


