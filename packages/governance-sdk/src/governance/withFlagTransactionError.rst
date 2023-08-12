packages/governance-sdk/src/governance/withFlagTransactionError.ts
==================================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import {
  PublicKey,
  SYSVAR_CLOCK_PUBKEY,
  TransactionInstruction,
} from '@solana/web3.js';
import { getGovernanceInstructionSchema } from './serialisation';
import { serialize } from 'borsh';
import { FlagTransactionErrorArgs } from './instructions';
import { PROGRAM_VERSION_V1 } from '../registry/constants';

export const withFlagTransactionError = (
  instructions: TransactionInstruction[],
  programId: PublicKey,
  programVersion: number,
  proposal: PublicKey,
  tokenOwnerRecord: PublicKey,
  governanceAuthority: PublicKey,
  proposalTransaction: PublicKey,
) => {
  const args = new FlagTransactionErrorArgs();
  const data = Buffer.from(
    serialize(getGovernanceInstructionSchema(programVersion), args),
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
      pubkey: proposalTransaction,
      isWritable: true,
      isSigner: false,
    },
  ];
  if (programVersion === PROGRAM_VERSION_V1) {
    keys.push({
      pubkey: SYSVAR_CLOCK_PUBKEY,
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
};


