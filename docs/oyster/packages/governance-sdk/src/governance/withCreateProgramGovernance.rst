packages/governance-sdk/src/governance/withCreateProgramGovernance.ts
=====================================================================

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
import { GovernanceConfig } from './accounts';
import { CreateProgramGovernanceArgs } from './instructions';
import { SYSTEM_PROGRAM_ID } from '../tools/sdk/runtime';
import { BPF_UPGRADE_LOADER_ID } from '../tools/sdk/bpfUpgradeableLoader';
import { withRealmConfigPluginAccounts } from './withRealmConfigPluginAccounts';
import { PROGRAM_VERSION_V1 } from '../registry/constants';

/** @deprecated */
export const withCreateProgramGovernance = async (
  instructions: TransactionInstruction[],
  programId: PublicKey,
  programVersion: number,
  realm: PublicKey,
  governedProgram: PublicKey,
  config: GovernanceConfig,
  transferUpgradeAuthority: boolean,
  programUpgradeAuthority: PublicKey,
  tokenOwnerRecord: PublicKey,
  payer: PublicKey,
  governanceAuthority: PublicKey,
  voterWeightRecord?: PublicKey,
) => {
  const args = new CreateProgramGovernanceArgs({
    config,
    transferUpgradeAuthority,
  });

  const data = Buffer.from(
    serialize(getGovernanceInstructionSchema(programVersion), args),
  );

  const [governanceAddress] = await PublicKey.findProgramAddress(
    [
      Buffer.from('program-governance'),
      realm.toBuffer(),
      governedProgram.toBuffer(),
    ],
    programId,
  );

  const [programDataAddress] = await PublicKey.findProgramAddress(
    [governedProgram.toBuffer()],
    BPF_UPGRADE_LOADER_ID,
  );

  const keys = [
    {
      pubkey: realm,
      isWritable: false,
      isSigner: false,
    },
    {
      pubkey: governanceAddress,
      isWritable: true,
      isSigner: false,
    },
    {
      pubkey: governedProgram,
      isWritable: false,
      isSigner: false,
    },
    {
      pubkey: programDataAddress,
      isWritable: true,
      isSigner: false,
    },
    {
      pubkey: programUpgradeAuthority,
      isWritable: false,
      isSigner: true,
    },
    {
      pubkey: tokenOwnerRecord,
      isWritable: false,
      isSigner: false,
    },
    {
      pubkey: payer,
      isWritable: true,
      isSigner: true,
    },
    {
      pubkey: BPF_UPGRADE_LOADER_ID,
      isWritable: false,
      isSigner: false,
    },
    {
      pubkey: SYSTEM_PROGRAM_ID,
      isWritable: false,
      isSigner: false,
    },
  ];

  if (programVersion === PROGRAM_VERSION_V1) {
    keys.push({
      pubkey: SYSVAR_RENT_PUBKEY,
      isWritable: false,
      isSigner: false,
    });
  }

  keys.push({
    pubkey: governanceAuthority,
    isWritable: false,
    isSigner: true,
  });

  await withRealmConfigPluginAccounts(
    keys,
    programId,
    realm,
    voterWeightRecord,
  );

  instructions.push(
    new TransactionInstruction({
      keys,
      programId,
      data,
    }),
  );

  return governanceAddress;
};


