test/fixtures/defaulted/mixin.ts
================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { defaulted, string, object, number } from '../../..'

export const Struct = defaulted(
  object({
    title: string(),
    version: number(),
  }),
  {
    title: 'Untitled',
  }
)

export const data = {
  version: 0,
}

export const output = {
  title: 'Untitled',
  version: 0,
}

export const coerce = true


