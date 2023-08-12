packages/js/src/errors/ReadApiError.ts
======================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import { MetaplexError } from './MetaplexError';

/** @group Errors */
export class ReadApiError extends MetaplexError {
  readonly name: string = 'ReadApiError';
  constructor(message: string, cause?: Error) {
    super(message, 'rpc', undefined, cause);
  }
}


