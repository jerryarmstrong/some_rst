src/client/util/new-account-with-lamports.js
============================================

Last edited: 2020-06-24 17:49:54

Contents:

.. code-block:: js

    // @flow

import {Account, Connection} from '@solana/web3.js';

import {sleep} from './sleep';

export async function newAccountWithLamports(
  connection: Connection,
  lamports: number = 1000000,
): Promise<Account> {
  const account = new Account();

  let retries = 10;
  await connection.requestAirdrop(account.publicKey, lamports);
  for (;;) {
    await sleep(500);
    if (lamports == (await connection.getBalance(account.publicKey))) {
      return account;
    }
    if (--retries <= 0) {
      break;
    }
    console.log('Airdrop retry ' + retries);
  }
  throw new Error(`Airdrop of ${lamports} failed`);
}


