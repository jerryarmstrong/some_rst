test/types/set.ts
=================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { assert, set, string } from '../..'
import { test } from '..'

test<Set<string>>((x) => {
  assert(x, set(string()))
  return x
})


