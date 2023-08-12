packages/js/src/utils/types.ts
==============================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    export type PartialKeys<T extends object, K extends keyof T = keyof T> = Omit<
  T,
  K
> &
  Partial<Pick<T, K>>;

export type RequiredKeys<T extends object, K extends keyof T = keyof T> = Omit<
  T,
  K
> &
  Required<Pick<T, K>>;

export type Option<T> = T | null;

export type Opaque<T, K> = T & { __opaque__: K };


