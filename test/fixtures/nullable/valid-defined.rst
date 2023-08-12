test/fixtures/nullable/valid-defined.ts
=======================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { number, nullable } from '../../..'

export const Struct = nullable(number())

export const data = 42

export const output = 42


