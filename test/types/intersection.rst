test/types/intersection.ts
==========================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { assert, intersection, object, string } from '../..'
import { test } from '..'

test<{ a: string } & { b: string }>((x) => {
  assert(x, intersection([object({ a: string() }), object({ b: string() })]))
  return x
})


