packages/governance/src/actions/insertInstruction.ts
====================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { Keypair, PublicKey, TransactionInstruction } from '@solana/web3.js';

import { InstructionData, Proposal } from '@solana/spl-governance';

import { withInsertTransaction } from '@solana/spl-governance';

import { sendTransactionWithNotifications } from '../tools/transactions';
import { RpcContext } from '@solana/spl-governance';
import { ProgramAccount } from '@solana/spl-governance';

export const insertInstruction = async (
  { connection, wallet, programId, programVersion, walletPubkey }: RpcContext,
  proposal: ProgramAccount<Proposal>,
  tokenOwnerRecord: PublicKey,
  index: number,
  optionIndex: number,
  holdUpTime: number,
  instructionData: InstructionData,
) => {
  let signers: Keypair[] = [];
  let instructions: TransactionInstruction[] = [];

  const governanceAuthority = walletPubkey;
  const payer = walletPubkey;

  const proposalInstructionAddress = await withInsertTransaction(
    instructions,
    programId,
    programVersion,
    proposal.account.governance,
    proposal.pubkey,
    tokenOwnerRecord,
    governanceAuthority,
    index,
    optionIndex,
    holdUpTime,
    [instructionData],
    payer,
  );

  await sendTransactionWithNotifications(
    connection,
    wallet,
    instructions,
    signers,
    'Adding instruction',
    'Instruction added',
  );

  return proposalInstructionAddress;
};


