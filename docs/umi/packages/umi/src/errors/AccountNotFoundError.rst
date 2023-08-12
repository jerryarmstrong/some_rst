packages/umi/src/errors/AccountNotFoundError.ts
===============================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    import { PublicKey } from '@metaplex-foundation/umi-public-keys';
import { SdkError } from './SdkError';

/** @category Errors */
export class AccountNotFoundError extends SdkError {
  readonly name: string = 'AccountNotFoundError';

  constructor(publicKey: PublicKey, accountType?: string, solution?: string) {
    const message = `${
      accountType
        ? `The account of type [${accountType}] was not found`
        : 'No account was found'
    } at the provided address [${publicKey}].${solution ? ` ${solution}` : ''}`;
    super(message);
  }
}


