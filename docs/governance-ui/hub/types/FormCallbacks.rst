hub/types/FormCallbacks.ts
==========================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    export type FormCallbacks<V extends object> = {
  [K in keyof V as `on${Capitalize<K extends string ? K : never>}Change`]+?: (
    value: V[K],
  ) => void;
};


