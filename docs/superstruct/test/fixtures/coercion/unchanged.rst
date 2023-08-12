test/fixtures/coercion/unchanged.ts
===================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { string, coercion } from '../../..'

export const Struct = coercion(string(), (x) => (x == null ? 'unknown' : x))

export const data = 'known'

export const output = 'known'

export const coerce = true


