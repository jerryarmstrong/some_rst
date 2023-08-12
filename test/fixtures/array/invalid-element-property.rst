test/fixtures/array/invalid-element-property.ts
===============================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { array, object, string } from '../../..'

export const Struct = array(object({ id: string() }))

export const data = [{ id: '1' }, { id: false }, { id: '3' }]

export const error = {
  value: false,
  type: 'string',
  path: [1, 'id'],
  branch: [data, data[1], data[1].id],
}


