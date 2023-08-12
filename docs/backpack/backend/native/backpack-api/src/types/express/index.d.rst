backend/native/backpack-api/src/types/express/index.d.ts
========================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    export {};

declare global {
  namespace Express {
    export interface Request {
      id?: string;
      jwt?: string;
    }
  }
}


