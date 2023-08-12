test/types/nullable.ts
======================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { assert, nullable, string, object } from '../..'
import { test } from '..'

test<string | null>((x) => {
  assert(x, nullable(string()))
  return x
})

test<{ a: string | null }>((x) => {
  assert(x, object({ a: nullable(string()) }))
  return x
})


