test/fixtures/optional/valid-defined.ts
=======================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { number, optional } from '../../..'

export const Struct = optional(number())

export const data = 42

export const output = 42


