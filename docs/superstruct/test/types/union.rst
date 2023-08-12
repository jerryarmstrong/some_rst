test/types/union.ts
===================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { assert, union, object, string } from '../..'
import { test } from '..'

test<{ a: string } | { b: string }>((x) => {
  assert(x, union([object({ a: string() }), object({ b: string() })]))
  return x
})


