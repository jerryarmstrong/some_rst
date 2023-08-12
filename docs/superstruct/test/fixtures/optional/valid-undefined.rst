test/fixtures/optional/valid-undefined.ts
=========================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { number, optional } from '../../..'

export const Struct = optional(number())

export const data = undefined

export const output = undefined


