test/types/map.ts
=================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { assert, map, string, number } from '../..'
import { test } from '..'

test<Map<string, number>>((x) => {
  assert(x, map(string(), number()))
  return x
})


