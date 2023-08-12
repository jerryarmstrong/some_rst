packages/library-legacy/src/utils/assert.ts
===========================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    export default function (
  condition: unknown,
  message?: string,
): asserts condition {
  if (!condition) {
    throw new Error(message || 'Assertion failed');
  }
}


