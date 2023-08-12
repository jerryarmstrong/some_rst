name-service/js/src/state.ts
============================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: ts

    import { Connection, PublicKey } from '@solana/web3.js';
import { deserializeUnchecked, Schema } from 'borsh';

export class NameRegistryState {
  static HEADER_LEN = 96;
  parentName: PublicKey;
  owner: PublicKey;
  class: PublicKey;
  data: Buffer | undefined;

  static schema: Schema = new Map([
    [
      NameRegistryState,
      {
        kind: 'struct',
        fields: [
          ['parentName', [32]],
          ['owner', [32]],
          ['class', [32]],
        ],
      },
    ],
  ]);
  constructor(obj: {
    parentName: Uint8Array;
    owner: Uint8Array;
    class: Uint8Array;
  }) {
    this.parentName = new PublicKey(obj.parentName);
    this.owner = new PublicKey(obj.owner);
    this.class = new PublicKey(obj.class);
  }

  public static async retrieve(
    connection: Connection,
    nameAccountKey: PublicKey
  ): Promise<NameRegistryState> {
    const nameAccount = await connection.getAccountInfo(
      nameAccountKey,
      'processed'
    );
    if (!nameAccount) {
      throw new Error('Invalid name account provided');
    }

    const res: NameRegistryState = deserializeUnchecked(
      this.schema,
      NameRegistryState,
      nameAccount.data
    );

    res.data = nameAccount.data?.slice(this.HEADER_LEN);

    return res;
  }
}


