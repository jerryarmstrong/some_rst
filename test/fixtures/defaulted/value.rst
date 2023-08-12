test/fixtures/defaulted/value.ts
================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { number, defaulted } from '../../..'

export const Struct = defaulted(number(), 42)

export const data = undefined

export const output = 42

export const coerce = true


