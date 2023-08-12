components/TreasuryAccount/LoadingRows.tsx
==========================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    import React from 'react'

const LoadingRows = () => {
  return (
    <div className="space-y-2">
      <div className="animate-pulse bg-bkg-3 h-12 rounded-md" />
      <div className="animate-pulse bg-bkg-3 h-12 rounded-md" />
      <div className="animate-pulse bg-bkg-3 h-12 rounded-md" />
    </div>
  )
}

export default LoadingRows


