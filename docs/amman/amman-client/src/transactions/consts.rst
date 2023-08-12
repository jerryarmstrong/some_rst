amman-client/src/transactions/consts.ts
=======================================

Last edited: 2022-11-03 12:19:53

Contents:

.. code-block:: ts

    import { ConfirmOptions } from '@solana/web3.js'

/**
 * Default options for sending and confirming a transaction
 * @category transactions
 */
export const defaultConfirmOptions: ConfirmOptions = {
  skipPreflight: true,
  preflightCommitment: 'confirmed',
  commitment: 'confirmed',
}


