tools/sdk/accounts.ts
=====================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import { ProgramAccount } from '@solana/spl-governance'
import { arrayToRecord } from '@tools/core/script'

/**
 * Maps the source array of account to a map keyed by pubkey of the accounts
 * @param accounts
 * @returns
 */
export function accountsToPubkeyMap<T>(accounts: ProgramAccount<T>[]) {
  return arrayToRecord(accounts, (a) => a.pubkey.toBase58())
}


