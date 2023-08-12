components/Divider.tsx
======================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: tsx

    import React from 'react'

const Divider: React.FC<{
  className?: string
  dashed?: boolean
}> = ({ className, dashed }) => (
  <div
    className={`border-b border-${
      dashed ? 'dashed' : 'solid'
    } opacity-20 w-full my-3 ${className}`}
  />
)

export default Divider


