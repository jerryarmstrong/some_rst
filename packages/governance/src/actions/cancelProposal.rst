packages/governance/src/actions/cancelProposal.ts
=================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { Keypair, PublicKey, TransactionInstruction } from '@solana/web3.js';

import { Proposal } from '@solana/spl-governance';

import { sendTransactionWithNotifications } from '../tools/transactions';
import { RpcContext } from '@solana/spl-governance';
import { ProgramAccount } from '@solana/spl-governance';

import { withCancelProposal } from '@solana/spl-governance';

export async function cancelProposal(
  { connection, wallet, programId, programVersion, walletPubkey }: RpcContext,
  realm: PublicKey,
  proposal: ProgramAccount<Proposal>,
) {
  let governanceAuthority = walletPubkey;

  let signers: Keypair[] = [];
  let instructions: TransactionInstruction[] = [];

  withCancelProposal(
    instructions,
    programId,
    programVersion,
    realm,
    proposal.account.governance,
    proposal.pubkey,
    proposal.account.tokenOwnerRecord,
    governanceAuthority,
  );

  await sendTransactionWithNotifications(
    connection,
    wallet,
    instructions,
    signers,
    'Cancelling proposal',
    'Proposal cancelled',
  );
}


