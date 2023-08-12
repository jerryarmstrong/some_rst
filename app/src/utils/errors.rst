app/src/utils/errors.ts
=======================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: ts

    export class OrderSideCollisionError extends Error {
  constructor(message: string, options?: any) {
    super(message, options);
    this.name = "OrderSideCollisionError";
  }
}


