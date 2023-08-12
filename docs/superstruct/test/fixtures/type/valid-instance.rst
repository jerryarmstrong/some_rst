test/fixtures/type/valid-instance.ts
====================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { type, string } from '../../..'

class Person {
  name: string

  constructor(name: string) {
    this.name = name
  }
}

export const Struct = type({
  name: string(),
})

export const data = new Person('john')

export const output = data


