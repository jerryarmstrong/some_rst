packages/governance-sdk/src/tools/script.ts
===========================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    export function getErrorMessage(ex: any) {
  if (ex instanceof Error) {
    return ex.message;
  }

  return JSON.stringify(ex);
}


