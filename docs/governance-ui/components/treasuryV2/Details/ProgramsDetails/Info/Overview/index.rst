components/treasuryV2/Details/ProgramsDetails/Info/Overview/index.tsx
=====================================================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    import React from 'react'

import { Programs } from '@models/treasury/Asset'

import Program from './Program'

interface Props {
  className?: string
  programs: Programs
}

export default function Overview(props: Props) {
  return (
    <section className={props.className}>
      {props.programs.list.map((program) => (
        <Program
          className="py-4 border-b border-white/10 mb-6 last:mb-0"
          key={program.address}
          program={program}
        />
      ))}
    </section>
  )
}


