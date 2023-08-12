packages/governance/src/views/proposal/components/instruction/buttons/flagInstructionErrorButton.tsx
====================================================================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import { BugOutlined } from '@ant-design/icons';
import { Button, Tooltip } from 'antd';
import React from 'react';
import { flagInstructionError } from '../../../../../actions/flagInstructionError';
import { useRpcContext } from '../../../../../hooks/useRpcContext';
import { PlayState } from './executeInstructionButton';

import {
  InstructionExecutionStatus,
  Proposal,
  ProposalTransaction,
  TokenOwnerRecord,
} from '@solana/spl-governance';
import { ProgramAccount } from '@solana/spl-governance';

export function FlagInstructionErrorButton({
  proposal,
  proposalInstruction,
  proposalAuthority,
  playState,
}: {
  proposal: ProgramAccount<Proposal>;
  proposalInstruction: ProgramAccount<ProposalTransaction>;
  proposalAuthority: ProgramAccount<TokenOwnerRecord> | undefined;
  playState: PlayState;
}) {
  const rpcContext = useRpcContext();

  if (
    playState !== PlayState.Error ||
    proposalInstruction.account.executionStatus ===
      InstructionExecutionStatus.Error ||
    !proposalAuthority
  ) {
    return null;
  }

  const onFlagError = async () => {
    try {
      await flagInstructionError(
        rpcContext,
        proposal,
        proposalInstruction.pubkey,
      );
    } catch {}
  };

  return (
    <Tooltip title="flag instruction as broken">
      <Button onClick={onFlagError}>
        <BugOutlined style={{ color: 'red' }} />
      </Button>
    </Tooltip>
  );
}


