test/fixtures/object/valid-opaque.ts
====================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { object } from '../../..'

export const Struct = object()

export const data = {
  a: 'string',
  b: 42,
}

export const output = {
  a: 'string',
  b: 42,
}


