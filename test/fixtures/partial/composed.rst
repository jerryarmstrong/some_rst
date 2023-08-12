test/fixtures/partial/composed.ts
=================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { partial, object, string, number } from '../../..'

export const Struct = partial(
  object({
    name: string(),
    age: number(),
  })
)

export const data = {
  name: 'john',
}

export const output = {
  name: 'john',
}


