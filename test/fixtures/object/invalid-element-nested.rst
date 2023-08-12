test/fixtures/object/invalid-element-nested.ts
==============================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { object, array, string } from '../../..'

export const Struct = object({
  name: string(),
  emails: array(string()),
})

export const data = {
  name: 'john',
  emails: ['name@example.com', false],
}

export const error = {
  value: false,
  type: 'string',
  path: ['emails', 1],
  branch: [data, data.emails, data.emails[1]],
}


