test/fixtures/set/valid.ts
==========================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { set, number } from '../../..'

export const Struct = set(number())

export const data = new Set([1, 2, 3])

export const output = new Set([1, 2, 3])


