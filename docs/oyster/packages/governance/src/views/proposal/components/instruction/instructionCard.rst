packages/governance/src/views/proposal/components/instruction/instructionCard.tsx
=================================================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import { DeleteOutlined } from '@ant-design/icons';
import { useWallet } from '@oyster/common';
import { Card, Button, Space } from 'antd';
import Meta from 'antd/lib/card/Meta';
import React, { useMemo, useState } from 'react';
import { LABELS } from '../../../../constants';
import {
  GovernanceAccountType,
  Proposal,
  ProposalTransaction,
  ProposalState,
  getGovernanceInstructionSchema,
} from '@solana/spl-governance';
import { serialize } from 'borsh';

import '../style.less';

import { removeInstruction } from '../../../../actions/removeInstruction';
import { useAccountChangeTracker } from '../../../../contexts/GovernanceContext';
import { useProposalAuthority } from '../../../../hooks/apiHooks';
import { useRpcContext } from '../../../../hooks/useRpcContext';
import { FlagInstructionErrorButton } from './buttons/flagInstructionErrorButton';
import {
  PlayState,
  ExecuteInstructionButton,
} from './buttons/executeInstructionButton';
import { DryRunInstructionButton } from './buttons/dryRunInstructionButton';
import { ProgramAccount } from '@solana/spl-governance';

export function InstructionCard({
  proposalInstruction,
  proposal,
  position,
}: {
  proposalInstruction: ProgramAccount<ProposalTransaction>;
  proposal: ProgramAccount<Proposal>;
  position: number;
}) {
  const { connected } = useWallet();
  const rpcContext = useRpcContext();
  const changeTracker = useAccountChangeTracker();

  const proposalAuthority = useProposalAuthority(
    proposal.account.tokenOwnerRecord,
  );

  const [tabKey, setTabKey] = useState('info');
  const [playing, setPlaying] = useState(
    proposalInstruction.account.executedAt
      ? PlayState.Played
      : PlayState.Unplayed,
  );

  const instructionDetails = useMemo(() => {
    const dataBase64 = Buffer.from(
      serialize(
        getGovernanceInstructionSchema(rpcContext.programVersion),
        proposalInstruction.account.getSingleInstruction(),
      ),
    ).toString('base64');

    return {
      programId: proposalInstruction.account.getSingleInstruction().programId,
      dataBase64: dataBase64,
    };
  }, [proposalInstruction, rpcContext.programVersion]);

  const contentList: Record<string, JSX.Element> = {
    info: (
      <Meta
        title={`${LABELS.PROGRAM_ID}: ${instructionDetails.programId}`}
        description={
          <>
            <p>{`${LABELS.INSTRUCTION}: ${instructionDetails.dataBase64}`}</p>
            <p>
              {LABELS.HOLD_UP_TIME_DAYS}:{' '}
              {proposalInstruction.account.holdUpTime / 86400}
            </p>
          </>
        }
      />
    ),
    data: <p className="wordwrap">{instructionDetails.dataBase64}</p>,
  };

  const isEditable =
    proposal.account.state === ProposalState.Draft && proposalAuthority;

  const deleteAction = () => {
    const onDelete = async () => {
      await removeInstruction(rpcContext, proposal, proposalInstruction.pubkey);
      changeTracker.notifyAccountRemoved(
        proposalInstruction.pubkey.toBase58(),
        GovernanceAccountType.ProposalInstructionV1,
      );
    };

    return (
      <Button onClick={onDelete} disabled={!connected} key="delete">
        <DeleteOutlined />
      </Button>
    );
  };

  return (
    <Card
      extra={
        <Space>
          <DryRunInstructionButton
            proposal={proposal}
            instructionData={proposalInstruction.account.getSingleInstruction()}
          ></DryRunInstructionButton>
          <FlagInstructionErrorButton
            playState={playing}
            proposal={proposal}
            proposalInstruction={proposalInstruction}
            proposalAuthority={proposalAuthority}
          ></FlagInstructionErrorButton>
          <ExecuteInstructionButton
            playing={playing}
            setPlaying={setPlaying}
            proposal={proposal}
            proposalInstruction={proposalInstruction}
          />
        </Space>
      }
      tabList={[
        { key: 'info', tab: 'Info' },
        { key: 'data', tab: 'Data' },
      ]}
      title={'Instruction #' + position}
      activeTabKey={tabKey}
      onTabChange={setTabKey}
      actions={isEditable ? [deleteAction()] : undefined}
    >
      {contentList[tabKey]}
    </Card>
  );
}


