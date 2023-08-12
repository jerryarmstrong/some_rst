examples/throwing-errors.js
===========================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: js

    import { object, number, string, assert } from 'superstruct'

// Define a struct to validate with.
const User = object({
  id: number(),
  name: string(),
  email: string(),
})

// Define data to be validated.
const data = {
  id: 1,
  name: true,
  email: 'jane@example.com',
}

// Validate the data with the `validate` method. In this case the `name`
// property is invalid, so an error will be thrown.
assert(data, User)


