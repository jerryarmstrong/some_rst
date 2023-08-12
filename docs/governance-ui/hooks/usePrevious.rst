hooks/usePrevious.ts
====================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import { useEffect, useRef } from 'react'

export function usePrevious(value) {
  const ref = useRef()
  useEffect(() => {
    ref.current = value
  })
  return ref.current as any
}


