packages/governance-sdk/src/governance/createSetRealmConfig.ts
==============================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { PublicKey, TransactionInstruction } from '@solana/web3.js';
import {
  GoverningTokenConfigAccountArgs,
  MintMaxVoteWeightSource,
} from './accounts';
import BN from 'bn.js';
import { withSetRealmConfig } from './withSetRealmConfig';

export async function createSetRealmConfig(
  programId: PublicKey,
  programVersion: number,
  realm: PublicKey,
  realmAuthority: PublicKey,
  councilMint: PublicKey | undefined,
  communityMintMaxVoteWeightSource: MintMaxVoteWeightSource,
  minCommunityTokensToCreateGovernance: BN,
  communityTokenConfig: GoverningTokenConfigAccountArgs | undefined,
  councilTokenConfig: GoverningTokenConfigAccountArgs | undefined,
  payer: PublicKey | undefined,
) {
  const instructions: TransactionInstruction[] = [];
  await withSetRealmConfig(
    instructions,
    programId,
    programVersion,
    realm,
    realmAuthority,
    councilMint,
    communityMintMaxVoteWeightSource,
    minCommunityTokensToCreateGovernance,
    communityTokenConfig,
    councilTokenConfig,
    payer,
  );

  return instructions[0];
}


