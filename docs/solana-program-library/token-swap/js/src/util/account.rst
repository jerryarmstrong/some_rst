token-swap/js/src/util/account.ts
=================================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: ts

    import type {Connection} from '@solana/web3.js';
import {PublicKey} from '@solana/web3.js';

export async function loadAccount(
  connection: Connection,
  address: PublicKey,
  programId: PublicKey,
): Promise<Buffer> {
  const accountInfo = await connection.getAccountInfo(address);
  if (accountInfo === null) {
    throw new Error('Failed to find account');
  }

  if (!accountInfo.owner.equals(programId)) {
    throw new Error(`Invalid owner: ${JSON.stringify(accountInfo.owner)}`);
  }

  return Buffer.from(accountInfo.data);
}


