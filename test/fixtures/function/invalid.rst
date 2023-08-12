test/fixtures/function/invalid.ts
=================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { func } from '../../..'

export const Struct = func()

export const data = false

export const error = {
  value: false,
  type: 'Function',
  path: [],
  branch: [data],
}


