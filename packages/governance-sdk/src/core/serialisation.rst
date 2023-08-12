packages/governance-sdk/src/core/serialisation.ts
=================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { AccountInfo, PublicKey } from '@solana/web3.js';

import { Schema } from 'borsh';
import { deserializeBorsh } from '../tools/borsh';
import { ProgramAccount } from '../tools/sdk/runtime';

export function BorshAccountParser(
  classFactory: any,
  getSchema: (accountType: number) => Schema,
): (pubKey: PublicKey, info: AccountInfo<Buffer>) => ProgramAccount<any> {
  return (pubKey: PublicKey, info: AccountInfo<Buffer>) => {
    const buffer = Buffer.from(info.data);
    const data = deserializeBorsh(
      getSchema(info.data[0]),
      classFactory,
      buffer,
    );

    return {
      pubkey: pubKey,
      owner: info.owner,
      account: data,
    } as ProgramAccount<any>;
  };
}


