src/util/new-system-account-with-airdrop.js
===========================================

Last edited: 2020-07-29 22:45:43

Contents:

.. code-block:: js

    // @flow

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


