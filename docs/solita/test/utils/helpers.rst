test/utils/helpers.ts
=====================

Last edited: 2023-07-06 15:09:22

Contents:

.. code-block:: ts

    import { inspect } from 'util'

export function deepInspect(obj: any) {
  return inspect(obj, { depth: 15, colors: true, getters: true })
}

export function deepLog(obj: any) {
  console.log(deepInspect(obj))
}


