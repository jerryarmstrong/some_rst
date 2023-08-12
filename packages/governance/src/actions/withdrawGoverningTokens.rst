packages/governance/src/actions/withdrawGoverningTokens.ts
==========================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { withWithdrawGoverningTokens } from '@solana/spl-governance';
import { PublicKey, TransactionInstruction } from '@solana/web3.js';
import { RpcContext } from '@solana/spl-governance';

import { sendTransactionWithNotifications } from '../tools/transactions';

export const withdrawGoverningTokens = async (
  { connection, wallet, programId, programVersion, walletPubkey }: RpcContext,
  realm: PublicKey,
  governingTokenDestination: PublicKey,
  governingTokenMint: PublicKey,
) => {
  let instructions: TransactionInstruction[] = [];

  await withWithdrawGoverningTokens(
    instructions,
    programId,
    programVersion,
    realm,
    governingTokenDestination,
    governingTokenMint,
    walletPubkey,
  );

  await sendTransactionWithNotifications(
    connection,
    wallet,
    instructions,
    [],
    'Withdrawing governing tokens',
    'Tokens have been withdrawn',
  );
};


