amman-client/src/relay/timeout.ts
=================================

Last edited: 2022-11-03 12:19:53

Contents:

.. code-block:: ts

    export function createTimeout(
  ms: number,
  rejectError: Error,
  reject: (reason: any) => void
) {
  return setTimeout(() => reject(rejectError), ms)
}


