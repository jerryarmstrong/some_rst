components/treasuryV2/Details/NoWalletSelected.tsx
==================================================

Last edited: 2023-08-11 18:13:34

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


