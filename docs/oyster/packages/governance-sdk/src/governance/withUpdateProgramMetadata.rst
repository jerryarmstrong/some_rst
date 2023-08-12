packages/governance-sdk/src/governance/withUpdateProgramMetadata.ts
===================================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { PublicKey, TransactionInstruction } from '@solana/web3.js';
import { getGovernanceInstructionSchema } from './serialisation';
import { serialize } from 'borsh';
import { UpdateProgramMetadataArgs } from './instructions';
import { getProgramMetadataAddress } from './accounts';
import { SYSTEM_PROGRAM_ID } from '../tools/sdk/runtime';

export const withUpdateProgramMetadata = async (
  instructions: TransactionInstruction[],
  programId: PublicKey,
  programVersion: number,

  payer: PublicKey,
) => {
  const args = new UpdateProgramMetadataArgs();
  const data = Buffer.from(
    serialize(getGovernanceInstructionSchema(programVersion), args),
  );

  const programMetadataAddress = await getProgramMetadataAddress(programId);

  const keys = [
    {
      pubkey: programMetadataAddress,
      isWritable: true,
      isSigner: false,
    },
    {
      pubkey: payer,
      isWritable: true,
      isSigner: true,
    },
    {
      pubkey: SYSTEM_PROGRAM_ID,
      isSigner: false,
      isWritable: false,
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


