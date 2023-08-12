test/types/object.ts
====================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { assert, object, optional, number, string } from '../..'
import { test } from '..'

test<Record<string, unknown>>((x) => {
  assert(x, object())
  return x
})

test<{ a: number }>((x) => {
  assert(x, object({ a: number() }))
  return x
})

test<{ a?: number }>((x) => {
  assert(x, object({ a: optional(number()) }))
  return x
})


