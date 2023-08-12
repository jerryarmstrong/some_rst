token-vault/js/test/utils/accounts.ts
=====================================

Last edited: 2022-10-11 23:41:10

Contents:

.. code-block:: ts

    import { Connection, PublicKey } from '@solana/web3.js';
import { Vault } from '../../src/generated';
import { strict as assert } from 'assert';

export async function getVault(connection: Connection, address: PublicKey) {
  const accountInfo = await connection.getAccountInfo(address);
  assert(accountInfo != null, `vault ${address} should exist`);
  return Vault.fromAccountInfo(accountInfo, 0)[0];
}


