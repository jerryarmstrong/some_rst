packages/sdk/core/src/accounts/ProgramAccount.ts
================================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import type { PublicKey } from '@solana/web3.js';

/**
 * Account and metadata
 */
export type ProgramAccount<T> = {
  pubkey: PublicKey;
  account: T;
  owner: PublicKey;
};


