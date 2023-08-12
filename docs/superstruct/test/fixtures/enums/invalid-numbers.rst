test/fixtures/enums/invalid-numbers.ts
======================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { enums } from '../../..'

export const Struct = enums([1, 2])

export const data = 'invalid'

export const error = {
  value: 'invalid',
  type: 'Enum<1,2>',
  path: [],
  branch: [data],
}


