packages/governance-sdk/src/governance/withCreateMintGovernance.ts
==================================================================

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
import { CreateMintGovernanceArgs } from './instructions';
import { TOKEN_PROGRAM_ID } from '../tools/sdk/splToken';
import { SYSTEM_PROGRAM_ID } from '../tools/sdk/runtime';
import { withRealmConfigPluginAccounts } from './withRealmConfigPluginAccounts';
import { PROGRAM_VERSION_V1 } from '../registry/constants';

/** @deprecated */
export const withCreateMintGovernance = async (
  instructions: TransactionInstruction[],
  programId: PublicKey,
  programVersion: number,
  realm: PublicKey,
  governedMint: PublicKey,
  config: GovernanceConfig,
  transferMintAuthorities: boolean,
  mintAuthority: PublicKey,
  tokenOwnerRecord: PublicKey,
  payer: PublicKey,
  governanceAuthority: PublicKey,
  voterWeightRecord?: PublicKey,
) => {
  const args = new CreateMintGovernanceArgs({
    config,
    transferMintAuthorities: transferMintAuthorities,
  });

  const data = Buffer.from(
    serialize(getGovernanceInstructionSchema(programVersion), args),
  );

  const [governanceAddress] = await PublicKey.findProgramAddress(
    [Buffer.from('mint-governance'), realm.toBuffer(), governedMint.toBuffer()],
    programId,
  );

  const keys = [
    {
      pubkey: realm, // 0
      isWritable: false,
      isSigner: false,
    },
    {
      pubkey: governanceAddress, // 1
      isWritable: true,
      isSigner: false,
    },
    {
      pubkey: governedMint, // 2
      isWritable: true,
      isSigner: false,
    },
    {
      pubkey: mintAuthority, // 3
      isWritable: false,
      isSigner: true,
    },
    {
      pubkey: tokenOwnerRecord, // 4
      isWritable: false,
      isSigner: false,
    },
    {
      pubkey: payer, // 5
      isWritable: true,
      isSigner: true,
    },
    {
      pubkey: TOKEN_PROGRAM_ID, // 6
      isWritable: false,
      isSigner: false,
    },
    {
      pubkey: SYSTEM_PROGRAM_ID, // 7
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


