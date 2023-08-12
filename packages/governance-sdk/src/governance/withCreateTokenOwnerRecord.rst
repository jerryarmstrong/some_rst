packages/governance-sdk/src/governance/withCreateTokenOwnerRecord.ts
====================================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { PublicKey, TransactionInstruction } from '@solana/web3.js';
import { getGovernanceInstructionSchema } from './serialisation';
import { serialize } from 'borsh';
import { CreateTokenOwnerRecordArgs } from './instructions';
import { getTokenOwnerRecordAddress } from './accounts';
import { SYSTEM_PROGRAM_ID } from '../tools/sdk/runtime';

export const withCreateTokenOwnerRecord = async (
  instructions: TransactionInstruction[],
  programId: PublicKey,
  programVersion: number,
  realm: PublicKey,
  governingTokenOwner: PublicKey,
  governingTokenMint: PublicKey,
  payer: PublicKey,
) => {
  const args = new CreateTokenOwnerRecordArgs();
  const data = Buffer.from(
    serialize(getGovernanceInstructionSchema(programVersion), args),
  );

  const tokenOwnerRecordAddress = await getTokenOwnerRecordAddress(
    programId,
    realm,
    governingTokenMint,
    governingTokenOwner,
  );

  const keys = [
    {
      pubkey: realm,
      isWritable: false,
      isSigner: false,
    },
    {
      pubkey: governingTokenOwner,
      isWritable: false,
      isSigner: false,
    },
    {
      pubkey: tokenOwnerRecordAddress,
      isWritable: true,
      isSigner: false,
    },
    {
      pubkey: governingTokenMint,
      isWritable: false,
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

  return tokenOwnerRecordAddress;
};


