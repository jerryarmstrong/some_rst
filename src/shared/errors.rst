src/shared/errors.ts
====================

Last edited: 2023-08-04 12:58:33

Contents:

.. code-block:: ts

    /* eslint-disable max-classes-per-file */
export class KinobiError extends Error {
  readonly name: string = 'KinobiError';
}

export class InvalidKinobiTreeError extends KinobiError {
  readonly name: string = 'InvalidKinobiTreeError';
}


