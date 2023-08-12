test/types/defaulted.ts
=======================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { assert, defaulted, string } from '../..'
import { test } from '..'

test<string>((x) => {
  assert(x, defaulted(string(), 'Untitled'))
  return x
})


