src/lib/base64/index.ts
=======================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    /**
 * Converts a base64 encoded string into its original form
 */
export function decode(a: string) {
  if (typeof window === 'undefined') {
    return Buffer.from(a, 'base64').toString('binary');
  } else {
    return window.atob(a);
  }
}

/**
 * Converts a string into a base64 encoded version
 */
export function encode(b: string) {
  if (typeof window === 'undefined') {
    return Buffer.from(b).toString('base64');
  } else {
    return window.btoa(b);
  }
}


