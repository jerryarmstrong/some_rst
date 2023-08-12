test/fixtures/masked/masked.ts
==============================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { masked, object, string } from '../../..'

export const Struct = masked(object({ name: string() }))

export const data = {
  id: '1',
  name: 'Jane',
}

export const output = {
  name: 'Jane',
}

export const coerce = true


