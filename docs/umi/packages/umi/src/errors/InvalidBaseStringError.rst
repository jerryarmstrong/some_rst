packages/umi/src/errors/InvalidBaseStringError.ts
=================================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    import { SdkError } from './SdkError';

/** @category Errors */
export class InvalidBaseStringError extends SdkError {
  readonly name: string = 'InvalidBaseStringError';

  constructor(value: string, base: number, cause?: Error) {
    const message = `Expected a string of base ${base}, got [${value}].`;
    super(message, cause);
  }
}


