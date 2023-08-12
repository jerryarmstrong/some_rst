models/voteRecords.ts
=====================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import {
  GovernanceAccountType,
  VoteKind,
  VoteRecord,
} from '@solana/spl-governance'

export function isYesVote(voteRecord: VoteRecord) {
  switch (voteRecord.accountType) {
    case GovernanceAccountType.VoteRecordV1: {
      return voteRecord.voteWeight?.yes && !voteRecord.voteWeight.yes.isZero()
    }
    case GovernanceAccountType.VoteRecordV2: {
      return voteRecord.vote?.voteType === VoteKind.Approve
    }
    default:
      throw new Error(`Invalid account type ${voteRecord.accountType} `)
  }
}

export function getVoteWeight(voteRecord: VoteRecord) {
  if (isYesVote(voteRecord)) {
    return voteRecord.getYesVoteWeight()
  }

  return voteRecord.getNoVoteWeight()
}


