test/fixtures/defaulted/nested.ts
=================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { defaulted, string, object } from '../../..'

export const Struct = object({
  title: defaulted(string(), 'Untitled'),
})

export const data = {}

export const output = {
  title: 'Untitled',
}

export const coerce = true


