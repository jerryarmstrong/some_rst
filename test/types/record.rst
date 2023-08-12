test/types/record.ts
====================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { assert, record, string, number } from '../..'
import { test } from '..'

test<Record<string, number>>((x) => {
  assert(x, record(string(), number()))
  return x
})


