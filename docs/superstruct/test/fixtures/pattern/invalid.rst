test/fixtures/pattern/invalid.ts
================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { string, pattern } from '../../..'

export const Struct = pattern(string(), /\d+/)

export const data = 'invalid'

export const error = {
  value: 'invalid',
  type: 'string & Pattern<\\d+>',
  path: [],
  branch: [data],
}


