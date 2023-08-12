packages/governance/src/views/realm/buttons/depositGoverningTokensButton.tsx
============================================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import { Button, Col, Modal, Row } from 'antd';
import React from 'react';
import { Realm } from '@solana/spl-governance';
import { LABELS } from '../../../constants';
import { hooks } from '@oyster/common';
import { ExclamationCircleOutlined } from '@ant-design/icons';
import { depositGoverningTokens } from '../../../actions/depositGoverningTokens';
import { PublicKey } from '@solana/web3.js';
import { useRpcContext } from '../../../hooks/useRpcContext';
import { ProgramAccount } from '@solana/spl-governance';

const { useAccountByMint } = hooks;

const { confirm } = Modal;
export function DepositGoverningTokensButton({
  realm,
  governingTokenMint,
  tokenName,
}: {
  realm: ProgramAccount<Realm> | undefined;
  governingTokenMint: PublicKey | undefined;
  tokenName?: string;
}) {
  const rpcContext = useRpcContext();

  const governingTokenAccount = useAccountByMint(governingTokenMint);

  if (!realm) {
    return null;
  }

  const isVisible =
    realm != null &&
    governingTokenAccount &&
    !governingTokenAccount.info.amount.isZero();

  return isVisible ? (
    <Button
      type="primary"
      onClick={() =>
        confirm({
          title: LABELS.DEPOSIT_TOKENS,
          icon: <ExclamationCircleOutlined />,
          content: (
            <Row>
              <Col span={24}>
                <p>{LABELS.DEPOSIT_TOKENS_QUESTION}</p>
              </Col>
            </Row>
          ),
          okText: LABELS.DEPOSIT,
          cancelText: LABELS.CANCEL,
          onOk: async () => {
            if (governingTokenAccount) {
              await depositGoverningTokens(
                rpcContext,
                realm!.pubkey,
                governingTokenAccount,
                governingTokenMint!,
              );
            }
          },
        })
      }
    >
      {LABELS.DEPOSIT_TOKENS(tokenName)}
    </Button>
  ) : null;
}


