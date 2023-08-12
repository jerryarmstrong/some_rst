packages/umi-storage-mock/src/errors.ts
=======================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    import { SdkError } from '@metaplex-foundation/umi';

/** @category Errors */
export class AssetNotFoundError extends SdkError {
  readonly name: string = 'AssetNotFoundError';

  constructor(location: string) {
    super(`The asset at [${location}] could not be found.`);
  }
}


