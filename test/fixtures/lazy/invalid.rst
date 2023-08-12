test/fixtures/lazy/invalid.ts
=============================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { lazy, string } from '../../..'

export const Struct = lazy(() => string())

export const data = 3

export const error = {
  value: 3,
  type: 'string',
  path: [],
  branch: [data],
}


