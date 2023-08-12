test/fixtures/length/invalid-string.ts
======================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { string, length } from '../../..'

export const Struct = length(string(), 1, 5)

export const data = ''

export const error = {
  value: '',
  type: 'string & Length<1,5>',
  path: [],
  branch: [data],
}


