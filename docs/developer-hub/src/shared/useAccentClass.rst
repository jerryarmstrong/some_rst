src/shared/useAccentClass.js
============================

Last edited: 2023-08-11 10:00:06

Contents:

.. code-block:: js

    import { useEffect } from "react"

export function useAccentClass(product) {
  useEffect(() => {
    document.querySelector('body').classList.forEach((className) => {
      if (className.startsWith('accent-')) {
        document.querySelector('body').classList.remove(className)
      }
    })
    if (product?.className) {
      document.querySelector('body').classList.add(product?.className)
    }
  })
}


