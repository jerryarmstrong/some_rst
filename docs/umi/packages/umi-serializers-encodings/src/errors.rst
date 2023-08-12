packages/umi-serializers-encodings/src/errors.ts
================================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    /** @category Errors */
export class InvalidBaseStringError extends Error {
  readonly name: string = 'InvalidBaseStringError';

  readonly cause?: Error;

  constructor(value: string, base: number, cause?: Error) {
    const message = `Expected a string of base ${base}, got [${value}].`;
    super(message);
    this.cause = cause;
  }
}


