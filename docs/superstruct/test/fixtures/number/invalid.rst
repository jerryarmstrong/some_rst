test/fixtures/number/invalid.ts
===============================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { number } from '../../..'

export const Struct = number()

export const data = 'invalid'

export const error = {
  value: 'invalid',
  type: 'number',
  path: [],
  branch: [data],
}


