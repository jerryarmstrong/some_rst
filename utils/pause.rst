utils/pause.ts
==============

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    export function pause(ms: number) {
  return new Promise<true>((resolve) => {
    setTimeout(() => resolve(true), ms)
  })
}


