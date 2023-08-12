components/treasuryV2/Details/NoWalletSelected.tsx
==================================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    import React from 'react'

interface Props {
  className?: string
}

export default function NoWalletSelected(props: Props) {
  return (
    <div className={props.className}>
      <div className="bg-bkg-1 p-10 flex items-center justify-center rounded h-52">
        No wallet selected
      </div>
    </div>
  )
}


