token-swap/js/src/util/new-system-account-with-airdrop.ts
=========================================================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: ts

    import {Account, Connection} from '@solana/web3.js';

/**
 * Create a new system account and airdrop it some lamports
 *
 * @private
 */
export async function newSystemAccountWithAirdrop(
  connection: Connection,
  lamports: number = 1,
): Promise<Account> {
  const account = new Account();
  await connection.requestAirdrop(account.publicKey, lamports);
  return account;
}


