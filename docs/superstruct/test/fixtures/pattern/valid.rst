test/fixtures/pattern/valid.ts
==============================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { string, pattern } from '../../..'

export const Struct = pattern(string(), /\d+/)

export const data = '123'

export const output = '123'


