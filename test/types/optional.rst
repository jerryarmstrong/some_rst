test/types/optional.ts
======================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { assert, optional, string, object } from '../..'
import { test } from '..'

test<string | undefined>((x) => {
  assert(x, optional(string()))
  return x
})

test<{ a?: string | undefined }>((x) => {
  assert(x, object({ a: optional(string()) }))
  return x
})


