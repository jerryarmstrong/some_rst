test/fixtures/dynamic/valid-reference.ts
========================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { assert, type, dynamic, literal, string, number } from '../../..'

const Entity = type({
  object: string(),
})

const User = type({
  object: literal('USER'),
  username: string(),
})

const Product = type({
  object: literal('PRODUCT'),
  price: number(),
})

const map = {
  USER: User,
  PRODUCT: Product,
}

export const Struct = dynamic((entity) => {
  assert(entity, Entity)
  return map[entity.object]
})

export const data = {
  object: 'PRODUCT',
  price: 1999,
}

export const output = {
  object: 'PRODUCT',
  price: 1999,
}


