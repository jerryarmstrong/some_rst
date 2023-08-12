packages/governance/src/views/governance/governanceView.tsx
===========================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import { Badge, Col, List, Row, Space, Typography } from 'antd';
import React, { useMemo, useState } from 'react';
import { useRealm } from '../../contexts/GovernanceContext';

import {
  useGovernance,
  useNativeTreasury,
  useProposalsByGovernance,
} from '../../hooks/apiHooks';
import './style.less'; // Don't remove this line, it will break dark mode if you do due to weird transpiling conditions
import { ProposalStateBadge } from '../proposal/components/header/proposalStateBadge';
import { useHistory } from 'react-router-dom';
import {
  ExplorerLink,
  TokenIcon,
  useConnectionConfig,
  useMint,
} from '@oyster/common';

import { useKeyParam } from '../../hooks/useKeyParam';
import { Proposal, ProposalState } from '@solana/spl-governance';
import { ClockCircleOutlined } from '@ant-design/icons';
import { GovernanceBadge } from '../../components/GovernanceBadge/governanceBadge';
import { getProposalUrl } from '../../tools/routeTools';
import { useRpcContext } from '../../hooks/useRpcContext';
import {
  formatMintNaturalAmountAsDecimal,
  formatMintSupplyFractionAsDecimalPercentage,
  getDaysFromTimestamp,
} from '../../tools/units';
import { GovernanceActionBar } from './buttons/governanceActionBar';
import { LAMPORTS_PER_SOL } from '@solana/web3.js';

const { Text } = Typography;

const PAGE_SIZE = 10;

export const GovernanceView = () => {
  const history = useHistory();
  const { programIdBase58 } = useRpcContext();

  const [, setPage] = useState(0);
  const { tokenMap } = useConnectionConfig();

  const governanceKey = useKeyParam();
  const governance = useGovernance(governanceKey);
  const realm = useRealm(governance?.account.realm);
  const proposals = useProposalsByGovernance(governanceKey);
  const communityMintInfo = useMint(realm?.account.communityMint);
  const nativeTreasury = useNativeTreasury(governance?.pubkey);

  const token = tokenMap.get(
    realm?.account.communityMint?.toBase58() || '',
  ) as any;
  const tokenBackground = token?.extensions?.background;

  const communityMint = realm?.account.communityMint?.toBase58() || '';

  const proposalItems = useMemo(() => {
    const compareProposals = (p1: Proposal, p2: Proposal) => {
      const p1Rank = p1.getStateSortRank();
      const p2Rank = p2.getStateSortRank();

      if (p1Rank > p2Rank) {
        return 1;
      } else if (p1Rank < p2Rank) {
        return -1;
      }

      const tsCompare = p1.getStateTimestamp() - p2.getStateTimestamp();

      // Show the proposals in voting state expiring earlier at the top
      return p1.state === ProposalState.Voting ? ~tsCompare : tsCompare;
    };

    return proposals
      .sort((p1, p2) => compareProposals(p2.account, p1.account))
      .map(p => ({
        key: p.pubkey.toBase58(),
        href: getProposalUrl(p.pubkey, programIdBase58),
        title: p.account.name,
        badge:
          p.account.state === ProposalState.Voting ? (
            <Badge count={<ClockCircleOutlined style={{ color: '#f5222d' }} />}>
              <TokenIcon mintAddress={p.account.governingTokenMint} size={30} />
            </Badge>
          ) : (
            <TokenIcon mintAddress={p.account.governingTokenMint} size={30} />
          ),
        proposal: p,
      }));
  }, [proposals, programIdBase58]);

  return (
    <Row
      style={{
        background: `url(${tokenBackground})`,
        minHeight: '100%',
        backgroundRepeat: 'repeat-y',
        backgroundSize: 'cover',
      }}
    >
      <Col flex="auto" xxl={15} xs={24} className="proposals-container">
        <div className="proposals-header">
          {governance && (
            <GovernanceBadge
              size={60}
              realm={realm}
              governance={governance}
              showVotingCount={false}
            ></GovernanceBadge>
          )}

          <div>
            <h1>{realm?.account.name}</h1>
            <h2>
              {governance && (
                <ExplorerLink
                  address={governance.account.governedAccount}
                  type="address"
                />
              )}
            </h2>
            <a
              href={tokenMap.get(communityMint)?.extensions?.website}
              target="_blank"
              rel="noopener noreferrer"
            >
              {tokenMap.get(communityMint)?.extensions?.website}
            </a>
            {governance && communityMintInfo && (
              <Space direction="vertical">
                <Space size="large">
                  <Space direction="vertical" size={0}>
                    <Text type="secondary">{`max voting time: ${getDaysFromTimestamp(
                      governance.account.config.maxVotingTime,
                    )} days`}</Text>
                    <Text type="secondary">{`yes vote threshold: ${governance.account.config.communityVoteThreshold.value}%`}</Text>
                  </Space>

                  <Space direction="vertical" size={0}>
                    <Text type="secondary">{`min instruction hold up time: ${getDaysFromTimestamp(
                      governance.account.config.minInstructionHoldUpTime,
                    )} days`}</Text>
                    <Text type="secondary">{`min tokens to create proposal: ${formatMintNaturalAmountAsDecimal(
                      communityMintInfo,
                      governance.account.config
                        .minCommunityTokensToCreateProposal,
                    )} (${formatMintSupplyFractionAsDecimalPercentage(
                      communityMintInfo,
                      governance.account.config
                        .minCommunityTokensToCreateProposal,
                    )})`}</Text>
                  </Space>
                </Space>
                {nativeTreasury && (
                  <div>
                    {`SOL: ${nativeTreasury.account.lamports / LAMPORTS_PER_SOL
                      }`}{' '}
                    <ExplorerLink
                      address={nativeTreasury.pubkey}
                      type="address"
                      length={3}
                    ></ExplorerLink>{' '}
                  </div>
                )}
              </Space>
            )}
          </div>

          <GovernanceActionBar
            governance={governance}
            realm={realm}
          ></GovernanceActionBar>
        </div>
        <h1 className="proposals-list-title">Proposals</h1>
        <List
          itemLayout="vertical"
          size="large"
          pagination={{
            onChange: page => {
              setPage(page);
            },
            pageSize: PAGE_SIZE,
          }}
          dataSource={proposalItems}
          renderItem={item => (
            <List.Item
              key={item.key}
              className="proposal-item"
              onClick={() => history.push(item.href)}
            >
              <List.Item.Meta
                avatar={item.badge}
                title={item.title}
                description={
                  <ProposalStateBadge
                    proposal={item.proposal}
                    governance={governance}
                  />
                }
              />
            </List.Item>
          )}
        />
      </Col>
    </Row>
  );
};


