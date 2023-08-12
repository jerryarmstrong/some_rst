packages/governance-sdk/src/governance/createSetGovernanceConfig.ts
===================================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { PublicKey, TransactionInstruction } from '@solana/web3.js';
import { GovernanceConfig } from './accounts';
import { SetGovernanceConfigArgs } from './instructions';
import { getGovernanceInstructionSchema } from './serialisation';
import { serialize } from 'borsh';

export function createSetGovernanceConfig(
  programId: PublicKey,
  programVersion: number,
  governance: PublicKey,
  governanceConfig: GovernanceConfig,
) {
  const args = new SetGovernanceConfigArgs({ config: governanceConfig });
  const data = Buffer.from(
    serialize(getGovernanceInstructionSchema(programVersion), args),
  );

  if (args.config.baseVotingTime < 3600) {
    throw new Error('baseVotingTime should be at least 1 hour');
  }

  const keys = [
    {
      pubkey: governance,
      isWritable: true,
      isSigner: true,
    },
  ];

  return new TransactionInstruction({
    keys,
    programId,
    data,
  });
}


