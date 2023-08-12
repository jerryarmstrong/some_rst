packages/governance/src/actions/updateProgramMetadata.ts
========================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { Keypair, TransactionInstruction } from '@solana/web3.js';

import { sendTransactionWithNotifications } from '../tools/transactions';
import { RpcContext } from '@solana/spl-governance';

import { withUpdateProgramMetadata } from '@solana/spl-governance';

export const updateProgramMetadata = async ({
  connection,
  wallet,
  programId,
  programVersion,
  walletPubkey,
}: RpcContext) => {
  let signers: Keypair[] = [];
  let instructions: TransactionInstruction[] = [];

  await withUpdateProgramMetadata(
    instructions,
    programId,
    programVersion,
    walletPubkey,
  );

  await sendTransactionWithNotifications(
    connection,
    wallet,
    instructions,
    signers,
    'Updating Program Metadata',
    'Program Metadata Updated',
  );
};


