test/fixtures/boolean/invalid.ts
================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { boolean } from '../../..'

export const Struct = boolean()

export const data = 'invalid'

export const error = {
  value: 'invalid',
  type: 'boolean',
  path: [],
  branch: [data],
}


