hooks/useInterval.tsx
=====================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    import { useRef, useEffect } from 'react'

export default function useInterval(callback, delay) {
  const savedCallback = useRef<() => void>()

  // Remember the latest callback.
  useEffect(() => {
    savedCallback.current = callback
  }, [callback])

  // Set up the interval.
  useEffect(() => {
    function tick() {
      savedCallback.current && savedCallback.current()
    }
    if (delay !== null) {
      const id = setInterval(tick, delay)
      return () => {
        clearInterval(id)
      }
    }
  }, [delay])
}


