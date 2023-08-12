test/fixtures/record/valid.ts
=============================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { record, string, number } from '../../..'

export const Struct = record(string(), number())

export const data = {
  a: 1,
  b: 2,
}

export const output = {
  a: 1,
  b: 2,
}


