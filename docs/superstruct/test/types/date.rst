test/types/date.ts
==================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { assert, date } from '../..'
import { test } from '..'

test<Date>((x) => {
  assert(x, date())
  return x
})


