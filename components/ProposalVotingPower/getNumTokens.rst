components/ProposalVotingPower/getNumTokens.ts
==============================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import type { ProgramAccount, TokenOwnerRecord } from '@solana/spl-governance'
import type { MintInfo } from '@solana/spl-token'
import { BigNumber } from 'bignumber.js'

import { getMintDecimalAmount } from '@tools/sdk/units'
import type {
  VoteRegistryVoterWeight,
  VoteNftWeight,
  SimpleGatedVoterWeight,
  VoterWeight,
} from '../../models/voteWeights'
import type { RealmInfo } from '../../models/registry/api'

type OwnVoterWeight =
  | VoteRegistryVoterWeight
  | VoteNftWeight
  | SimpleGatedVoterWeight
  | VoterWeight

export default function getNumTokens(
  _ownVoterWeight: OwnVoterWeight,
  depositTokenRecord?: ProgramAccount<TokenOwnerRecord>,
  mint?: MintInfo,
  _realmInfo?: RealmInfo
) {
  if (depositTokenRecord && mint) {
    return getMintDecimalAmount(
      mint,
      depositTokenRecord.account.governingTokenDepositAmount
    )
  }

  return new BigNumber('0')
}


