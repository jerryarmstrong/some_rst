packages/umi/src/errors/SdkError.ts
===================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    import { UmiError } from './UmiError';

/** @category Errors */
export class SdkError extends UmiError {
  readonly name: string = 'SdkError';

  constructor(message: string, cause?: Error) {
    super(message, 'sdk', undefined, cause);
  }
}


