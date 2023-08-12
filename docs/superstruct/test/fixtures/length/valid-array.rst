test/fixtures/length/valid-array.ts
===================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { number, array, length } from '../../..'

export const Struct = length(array(number()), 1, 5)

export const data = [1, 2, 3]

export const output = [1, 2, 3]


