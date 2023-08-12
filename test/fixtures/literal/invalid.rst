test/fixtures/literal/invalid.ts
================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { literal } from '../../..'

export const Struct = literal(42)

export const data = false

export const error = {
  value: false,
  type: 'Literal<42>',
  path: [],
  branch: [data],
}


