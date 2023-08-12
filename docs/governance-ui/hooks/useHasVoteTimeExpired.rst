hooks/useHasVoteTimeExpired.ts
==============================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import { Governance, Proposal } from '@solana/spl-governance'
import { ProgramAccount } from '@solana/spl-governance'
import { useIsBeyondTimestamp } from './useIsBeyondTimestamp'

export const useHasVoteTimeExpired = (
  governance: ProgramAccount<Governance> | undefined,
  proposal: ProgramAccount<Proposal>
) => {
  return useIsBeyondTimestamp(
    proposal
      ? proposal.account.isVoteFinalized()
        ? 0 // If vote is finalized then set the timestamp to 0 to make it expired
        : proposal.account.votingAt && governance
        ? proposal.account.votingAt.toNumber() +
          governance.account.config.baseVotingTime
        : undefined
      : undefined
  )
}


