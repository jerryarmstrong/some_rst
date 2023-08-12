test/fixtures/date/invalid.ts
=============================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { date } from '../../..'

export const Struct = date()

export const data = 'invalid'

export const error = {
  value: 'invalid',
  type: 'Date',
  path: [],
  branch: [data],
}


