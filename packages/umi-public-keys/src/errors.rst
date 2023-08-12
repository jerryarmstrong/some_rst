packages/umi-public-keys/src/errors.ts
======================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    /** @category Errors */
export class InvalidPublicKeyError extends Error {
  readonly name: string = 'InvalidPublicKeyError';

  readonly invalidPublicKey: string;

  constructor(invalidPublicKey: string, reason?: string) {
    reason = reason ? `. ${reason}` : '';
    super(`The provided public key is invalid: ${invalidPublicKey}${reason}`);
    this.invalidPublicKey = invalidPublicKey;
  }
}


