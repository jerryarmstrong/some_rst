src/shared/useLightense.js
==========================

Last edited: 2023-08-11 10:00:06

Contents:

.. code-block:: js

    import Lightense from 'lightense-images'
import { useEffect } from "react"

export function useLightense() {
  useEffect(() => Lightense('img:not(.no-lightense),.lightense'))
}


