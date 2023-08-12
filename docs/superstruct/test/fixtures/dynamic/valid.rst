test/fixtures/dynamic/valid.ts
==============================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { dynamic, string } from '../../..'

export const Struct = dynamic(() => string())

export const data = 'valid'

export const output = 'valid'


