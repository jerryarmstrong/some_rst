test/fixtures/tuple/valid.ts
============================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { tuple, string, number } from '../../..'

export const Struct = tuple([string(), number()])

export const data = ['A', 1]

export const output = ['A', 1]


