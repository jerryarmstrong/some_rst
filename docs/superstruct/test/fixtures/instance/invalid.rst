test/fixtures/instance/invalid.ts
=================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { instance } from '../../..'

export const Struct = instance(Array)

export const data = false

export const error = {
  value: false,
  type: 'InstanceOf<Array>',
  path: [],
  branch: [data],
}


