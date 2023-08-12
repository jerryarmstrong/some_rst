src/components/diagrams/useFullscreen.js
========================================

Last edited: 2023-08-11 10:00:06

Contents:

.. code-block:: js

    import { useCallback, useEffect, useState } from 'react'
import { useReactFlow } from 'reactflow'

export function useFullscreen() {
  const { fitView } = useReactFlow()
  const [fullscreen, setFullscreen] = useState(false)
  const toggleFullscreen = useCallback(() => {
    setFullscreen(!fullscreen)
    setTimeout(fitView, 20)
  }, [fullscreen, fitView])

  useEffect(() => {
    const handleEsc = (event) => {
      if (event.keyCode === 27 && fullscreen) {
        toggleFullscreen()
      }
    }
    window.addEventListener('keydown', handleEsc)
    return () => window.removeEventListener('keydown', handleEsc)
  }, [fullscreen, toggleFullscreen])

  return [fullscreen, toggleFullscreen]
}


