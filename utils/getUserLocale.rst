utils/getUserLocale.ts
======================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    /**
 * Get the user's locale using values on the browser. If unsuccessful, default
 * to `'en-US'`.
 */
export function getUserLocale() {
  if (
    typeof window === 'undefined' ||
    typeof window.navigator === 'undefined'
  ) {
    return 'en-US'
  }

  if (window.navigator.languages?.length) {
    return window.navigator.languages[0]
  }

  return window.navigator.language || 'en-US'
}


