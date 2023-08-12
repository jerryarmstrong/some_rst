js/packages/common/src/models/packs/instructions/activate.ts
============================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import { PublicKey, TransactionInstruction } from '@solana/web3.js';
import { serialize } from 'borsh';

import { programIds, toPublicKey } from '../../../utils';
import { ActivatePackArgs, PACKS_SCHEMA } from '../../../actions/packs';

interface Params {
  packSetKey: PublicKey;
  authority: string;
}

export async function activate({
  packSetKey,
  authority,
}: Params): Promise<TransactionInstruction> {
  const PROGRAM_IDS = programIds();

  const value = new ActivatePackArgs();
  const data = Buffer.from(serialize(PACKS_SCHEMA, value));

  const keys = [
    // pack_set
    {
      pubkey: toPublicKey(packSetKey),
      isSigner: false,
      isWritable: true,
    },
    // signer authority
    {
      pubkey: toPublicKey(authority),
      isSigner: true,
      isWritable: false,
    },
  ];

  return new TransactionInstruction({
    keys,
    programId: toPublicKey(PROGRAM_IDS.pack_create),
    data,
  });
}


