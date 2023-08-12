packages/governance-sdk/src/governance/withWithdrawGoverningTokens.ts
=====================================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { PublicKey, TransactionInstruction } from '@solana/web3.js';
import { getGovernanceInstructionSchema } from './serialisation';
import { serialize } from 'borsh';
import { WithdrawGoverningTokensArgs } from './instructions';
import { GOVERNANCE_PROGRAM_SEED } from './accounts';
import { TOKEN_PROGRAM_ID } from '../tools/sdk/splToken';
import { withV3RealmConfigAccount } from './tools';

export const withWithdrawGoverningTokens = async (
  instructions: TransactionInstruction[],
  programId: PublicKey,
  programVersion: number,
  realm: PublicKey,
  governingTokenDestination: PublicKey,
  governingTokenMint: PublicKey,
  governingTokenOwner: PublicKey,
) => {
  const args = new WithdrawGoverningTokensArgs();
  const data = Buffer.from(
    serialize(getGovernanceInstructionSchema(programVersion), args),
  );

  const [tokenOwnerRecordAddress] = await PublicKey.findProgramAddress(
    [
      Buffer.from(GOVERNANCE_PROGRAM_SEED),
      realm.toBuffer(),
      governingTokenMint.toBuffer(),
      governingTokenOwner.toBuffer(),
    ],
    programId,
  );

  const [governingTokenHoldingAddress] = await PublicKey.findProgramAddress(
    [
      Buffer.from(GOVERNANCE_PROGRAM_SEED),
      realm.toBuffer(),
      governingTokenMint.toBuffer(),
    ],
    programId,
  );

  const keys = [
    { pubkey: realm, isWritable: false, isSigner: false },
    {
      pubkey: governingTokenHoldingAddress,
      isWritable: true,
      isSigner: false,
    },
    {
      pubkey: governingTokenDestination,
      isWritable: true,
      isSigner: false,
    },
    {
      pubkey: governingTokenOwner,
      isWritable: false,
      isSigner: true,
    },
    {
      pubkey: tokenOwnerRecordAddress,
      isWritable: true,
      isSigner: false,
    },
    {
      pubkey: TOKEN_PROGRAM_ID,
      isWritable: false,
      isSigner: false,
    },
  ];

  await withV3RealmConfigAccount(keys, programId, programVersion, realm);

  instructions.push(
    new TransactionInstruction({
      keys,
      programId,
      data,
    }),
  );
};


