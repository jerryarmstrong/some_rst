packages/governance-sdk/src/governance/withRefundProposalDeposit.ts
===================================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { PublicKey, TransactionInstruction } from '@solana/web3.js';
import { getGovernanceInstructionSchema } from './serialisation';
import { serialize } from 'borsh';
import { RefundProposalDepositArgs } from './instructions';
import { getProposalDepositAddress } from './accounts';

export const withRefundProposalDeposit = async (
  instructions: TransactionInstruction[],
  programId: PublicKey,
  programVersion: number,
  proposalPk: PublicKey,
  proposalDepositPayerPk: PublicKey,
) => {
  const args = new RefundProposalDepositArgs();
  const data = Buffer.from(
    serialize(getGovernanceInstructionSchema(programVersion), args),
  );

  const proposalDepositAddress = await getProposalDepositAddress(
    programId,
    proposalPk,
    proposalDepositPayerPk,
  );

  const keys = [
    {
      pubkey: proposalPk,
      isWritable: false,
      isSigner: false,
    },
    {
      pubkey: proposalDepositAddress,
      isWritable: true,
      isSigner: false,
    },
    {
      pubkey: proposalDepositPayerPk,
      isWritable: true,
      isSigner: false,
    },
  ];

  instructions.push(
    new TransactionInstruction({
      keys,
      programId,
      data,
    }),
  );
};


