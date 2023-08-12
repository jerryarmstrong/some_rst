clients/js/src/errors.ts
========================

Last edited: 2023-08-11 07:39:15

Contents:

.. code-block:: ts

    import { UmiError } from '@metaplex-foundation/umi';

export class TokenMetadataError extends UmiError {
  readonly name: string = 'TokenMetadataError';

  constructor(message: string, cause?: Error) {
    super(message, 'plugin', 'Token Metadata', cause);
  }
}


