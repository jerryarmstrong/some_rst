test/fixtures/object/invalid-opaque.ts
======================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { object } from '../../..'

export const Struct = object()

export const data = 'invalid'

export const error = {
  value: 'invalid',
  type: 'Object',
  path: [],
  branch: [data],
}


