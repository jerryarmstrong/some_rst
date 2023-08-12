test/fixtures/enums/invalid-strings.ts
======================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { enums } from '../../..'

export const Struct = enums(['one', 'two'])

export const data = 'invalid'

export const error = {
  value: 'invalid',
  type: 'Enum<"one","two">',
  path: [],
  branch: [data],
}


