packages/governance-sdk/src/governance/withAddSignatory.ts
==========================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import {
  PublicKey,
  SYSVAR_RENT_PUBKEY,
  TransactionInstruction,
} from '@solana/web3.js';
import { getGovernanceInstructionSchema } from './serialisation';
import { serialize } from 'borsh';
import { AddSignatoryArgs } from './instructions';
import { getSignatoryRecordAddress } from './accounts';
import { SYSTEM_PROGRAM_ID } from '../tools/sdk/runtime';
import { PROGRAM_VERSION_V1 } from '../registry/constants';

export const withAddSignatory = async (
  instructions: TransactionInstruction[],
  programId: PublicKey,
  programVersion: number,
  proposal: PublicKey,
  tokenOwnerRecord: PublicKey,
  governanceAuthority: PublicKey,
  signatory: PublicKey,
  payer: PublicKey,
) => {
  const args = new AddSignatoryArgs({ signatory });
  const data = Buffer.from(
    serialize(getGovernanceInstructionSchema(programVersion), args),
  );

  const signatoryRecordAddress = await getSignatoryRecordAddress(
    programId,
    proposal,
    signatory,
  );

  const keys = [
    {
      pubkey: proposal,
      isWritable: true,
      isSigner: false,
    },
    {
      pubkey: tokenOwnerRecord,
      isWritable: false,
      isSigner: false,
    },
    {
      pubkey: governanceAuthority,
      isWritable: false,
      isSigner: true,
    },
    {
      pubkey: signatoryRecordAddress,
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

  if (programVersion === PROGRAM_VERSION_V1) {
    keys.push({
      pubkey: SYSVAR_RENT_PUBKEY,
      isSigner: false,
      isWritable: false,
    });
  }

  instructions.push(
    new TransactionInstruction({
      keys,
      programId,
      data,
    }),
  );

  return signatoryRecordAddress;
};


