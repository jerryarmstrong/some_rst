test/fixtures/empty/invalid-string.ts
=====================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { string, empty } from '../../..'

export const Struct = empty(string())

export const data = 'invalid'

export const error = {
  value: 'invalid',
  type: 'string & Empty',
  path: [],
  branch: [data],
}


