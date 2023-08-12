packages/umi/src/errors/UnexpectedAccountError.ts
=================================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    import { PublicKey } from '@metaplex-foundation/umi-public-keys';
import { SdkError } from './SdkError';

/** @category Errors */
export class UnexpectedAccountError extends SdkError {
  readonly name: string = 'UnexpectedAccountError';

  constructor(publicKey: PublicKey, expectedType: string, cause?: Error) {
    const message =
      `The account at the provided address [${publicKey}] ` +
      `is not of the expected type [${expectedType}].`;
    super(message, cause);
  }
}


