test/fixtures/masked/not-masked.ts
==================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { masked, object, string } from '../../..'

export const Struct = masked(object({ name: string() }))

export const data = false

export const error = {
  type: 'Object<{name}>',
  value: false,
  path: [],
  branch: [data],
}

export const coerce = true


