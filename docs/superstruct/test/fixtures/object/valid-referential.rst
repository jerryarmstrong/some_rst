test/fixtures/object/valid-referential.ts
=========================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { object, string, pattern, refinement } from '../../..'

const Section = pattern(string(), /^\d+(\.\d+)*$/)

export const Struct = object({
  section: Section,
  subsection: refinement(Section, 'Subsection', (value, ctx) => {
    const { branch } = ctx
    const parent = branch[0]
    return value.startsWith(`${parent.section}.`)
  }),
})

export const data = {
  section: '1',
  subsection: '1.1',
}

export const output = {
  section: '1',
  subsection: '1.1',
}


