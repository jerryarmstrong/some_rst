packages/governance/src/actions/executeInstruction.ts
=====================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { Keypair, TransactionInstruction } from '@solana/web3.js';

import { Proposal, ProposalTransaction } from '@solana/spl-governance';

import { withExecuteTransaction } from '@solana/spl-governance';
import { sendTransactionWithNotifications } from '../tools/transactions';
import { RpcContext } from '@solana/spl-governance';
import { ProgramAccount } from '@solana/spl-governance';

export const executeInstruction = async (
  { connection, wallet, programId, programVersion }: RpcContext,
  proposal: ProgramAccount<Proposal>,
  instruction: ProgramAccount<ProposalTransaction>,
) => {
  let signers: Keypair[] = [];
  let instructions: TransactionInstruction[] = [];

  await withExecuteTransaction(
    instructions,
    programId,
    programVersion,
    proposal.account.governance,
    proposal.pubkey,
    instruction.pubkey,
    instruction.account.getAllInstructions(),
  );

  await sendTransactionWithNotifications(
    connection,
    wallet,
    instructions,
    signers,
    'Executing instruction',
    'Instruction executed',
  );
};


