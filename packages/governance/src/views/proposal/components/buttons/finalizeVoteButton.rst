packages/governance/src/views/proposal/components/buttons/finalizeVoteButton.tsx
================================================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import { useWallet } from '@oyster/common';
import { Button } from 'antd';
import React from 'react';
import { LABELS } from '../../../../constants';
import { Governance, Proposal, ProposalState } from '@solana/spl-governance';
import { finalizeVote } from '../../../../actions/finalizeVote';
import { useRpcContext } from '../../../../hooks/useRpcContext';
import { ProgramAccount } from '@solana/spl-governance';

export function FinalizeVoteButton({
  governance,
  proposal,
  hasVoteTimeExpired,
}: {
  governance: ProgramAccount<Governance>;
  proposal: ProgramAccount<Proposal>;
  hasVoteTimeExpired: boolean | undefined;
}) {
  const { connected } = useWallet();
  const rpcContext = useRpcContext();

  const isVisible =
    hasVoteTimeExpired === true &&
    connected &&
    proposal.account.state === ProposalState.Voting;

  return isVisible ? (
    <Button
      type="primary"
      onClick={async () => {
        try {
          await finalizeVote(rpcContext, governance.account.realm, proposal);
        } catch (ex) {
          console.error(ex);
        }
      }}
    >
      {LABELS.FINALIZE_VOTE}
    </Button>
  ) : null;
}


