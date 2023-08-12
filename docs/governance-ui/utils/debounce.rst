utils/debounce.tsx
==================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    class Debounce {
  typingTimeout: null | ReturnType<typeof setTimeout>
  debounce: Debounce
  constructor() {
    this.typingTimeout = null
    return this.debounce
  }
  debounceFcn = (callback, timeoutDuration = 900) => {
    if (!callback) {
      console.log('missing argument callback')
    }
    if (this.typingTimeout) {
      clearTimeout(this.typingTimeout)
    }
    this.typingTimeout = setTimeout(() => {
      callback()
    }, timeoutDuration)
  }
}
export const debounce = new Debounce()


