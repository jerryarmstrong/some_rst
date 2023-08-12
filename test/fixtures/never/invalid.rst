test/fixtures/never/invalid.ts
==============================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { never } from '../../..'

export const Struct = never()

export const data = true

export const error = {
  value: true,
  type: 'never',
  path: [],
  branch: [data],
}


