packages/governance-sdk/src/governance/tools.ts
===============================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { AccountMeta, PublicKey } from '@solana/web3.js';
import BN from 'bn.js';
import { PROGRAM_VERSION_V2, PROGRAM_VERSION_V3 } from '../registry/constants';
import {
  getRealmConfigAddress,
  GoverningTokenConfigAccountArgs,
  GoverningTokenConfigArgs,
  GoverningTokenType,
  MintMaxVoteWeightSource,
  RealmConfigArgs,
} from './accounts';
import { GoverningTokenRole } from './enums';

function assertValidTokenConfigArgs(
  programVersion: number,
  tokenConfigArgs: GoverningTokenConfigAccountArgs | undefined,
  tokenKind: GoverningTokenRole,
) {
  if (tokenConfigArgs) {
    if (programVersion < PROGRAM_VERSION_V2) {
      throw new Error(
        `Governing token config is not supported in version ${programVersion}`,
      );
    } else if (programVersion == PROGRAM_VERSION_V2) {
      if (tokenKind == GoverningTokenRole.Council) {
        throw new Error(
          `Council token config is not supported in version ${programVersion}`,
        );
      }

      if (tokenConfigArgs.tokenType != GoverningTokenType.Liquid) {
        throw new Error(
          `Community token type ${tokenConfigArgs.tokenType} is not supported in veriosn ${programVersion}`,
        );
      }
    }
  }
}

export function createRealmConfigArgs(
  programVersion: number,
  councilMint: PublicKey | undefined,
  communityMintMaxVoteWeightSource: MintMaxVoteWeightSource,
  minCommunityWeightToCreateGovernance: BN,
  communityTokenConfig?: GoverningTokenConfigAccountArgs | undefined,
  councilTokenConfig?: GoverningTokenConfigAccountArgs | undefined,
) {
  assertValidTokenConfigArgs(
    programVersion,
    communityTokenConfig,
    GoverningTokenRole.Community,
  );
  assertValidTokenConfigArgs(
    programVersion,
    councilTokenConfig,
    GoverningTokenRole.Council,
  );

  return new RealmConfigArgs({
    useCouncilMint: councilMint !== undefined,
    minCommunityTokensToCreateGovernance: minCommunityWeightToCreateGovernance,
    communityMintMaxVoteWeightSource,

    // VERSION == 2
    useCommunityVoterWeightAddin:
      communityTokenConfig?.voterWeightAddin !== undefined,
    useMaxCommunityVoterWeightAddin:
      communityTokenConfig?.maxVoterWeightAddin !== undefined,

    // VERSION >= 3
    communityTokenConfigArgs: new GoverningTokenConfigArgs({
      useVoterWeightAddin: communityTokenConfig?.voterWeightAddin !== undefined,
      useMaxVoterWeightAddin:
        communityTokenConfig?.maxVoterWeightAddin !== undefined,
      tokenType: communityTokenConfig?.tokenType ?? GoverningTokenType.Liquid,
    }),
    councilTokenConfigArgs: new GoverningTokenConfigArgs({
      useVoterWeightAddin: councilTokenConfig?.voterWeightAddin !== undefined,
      useMaxVoterWeightAddin:
        councilTokenConfig?.maxVoterWeightAddin !== undefined,
      tokenType: councilTokenConfig?.tokenType ?? GoverningTokenType.Liquid,
    }),
  });
}

export function withTokenConfigAccounts(
  keys: Array<AccountMeta>,
  communityTokenConfig?: GoverningTokenConfigAccountArgs | undefined,
  councilTokenConfig?: GoverningTokenConfigAccountArgs | undefined,
) {
  if (communityTokenConfig?.voterWeightAddin) {
    keys.push({
      pubkey: communityTokenConfig.voterWeightAddin,
      isWritable: false,
      isSigner: false,
    });
  }

  if (communityTokenConfig?.maxVoterWeightAddin) {
    keys.push({
      pubkey: communityTokenConfig.maxVoterWeightAddin,
      isWritable: false,
      isSigner: false,
    });
  }

  if (councilTokenConfig?.voterWeightAddin) {
    keys.push({
      pubkey: councilTokenConfig.voterWeightAddin,
      isWritable: false,
      isSigner: false,
    });
  }

  if (councilTokenConfig?.maxVoterWeightAddin) {
    keys.push({
      pubkey: councilTokenConfig.maxVoterWeightAddin,
      isWritable: false,
      isSigner: false,
    });
  }
}

export async function withV3RealmConfigAccount(
  keys: Array<AccountMeta>,
  programId: PublicKey,
  programVersion: number,
  realm: PublicKey,
) {
  if (programVersion >= PROGRAM_VERSION_V3) {
    const realmConfigMeta = {
      pubkey: await getRealmConfigAddress(programId, realm),
      isSigner: false,
      isWritable: true,
    };

    keys.push(realmConfigMeta);
  }
}


