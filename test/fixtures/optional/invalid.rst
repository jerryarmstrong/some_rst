test/fixtures/optional/invalid.ts
=================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { number, optional } from '../../..'

export const Struct = optional(number())

export const data = 'invalid'

export const error = {
  value: 'invalid',
  type: 'number',
  path: [],
  branch: [data],
}


