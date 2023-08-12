packages/js/src/types/HasDriver.ts
==================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    export type HasDriver<T> = {
  driver: () => T;
  setDriver: (newDriver: T) => void;
};


