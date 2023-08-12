test/fixtures/partial/valid-full.ts
===================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { partial, string, number } from '../../..'

export const Struct = partial({
  name: string(),
  age: number(),
})

export const data = {
  name: 'john',
  age: 42,
}

export const output = {
  name: 'john',
  age: 42,
}


