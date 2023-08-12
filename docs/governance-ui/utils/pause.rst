utils/pause.ts
==============

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    export function pause(ms: number) {
  return new Promise<true>((resolve) => {
    setTimeout(() => resolve(true), ms)
  })
}


