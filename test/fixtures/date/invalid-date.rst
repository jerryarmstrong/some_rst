test/fixtures/date/invalid-date.ts
==================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { date } from '../../..'

export const Struct = date()

export const data = new Date('invalid')

export const error = {
  value: data,
  type: 'Date',
  path: [],
  branch: [data],
}


