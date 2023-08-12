hooks/useProposal.tsx
=====================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: tsx

    import { useRouteProposalQuery } from './queries/proposal'
import { useGovernanceByPubkeyQuery } from './queries/governance'

export const useProposalGovernanceQuery = () => {
  const proposal = useRouteProposalQuery().data?.result
  return useGovernanceByPubkeyQuery(proposal?.account.governance)
}


