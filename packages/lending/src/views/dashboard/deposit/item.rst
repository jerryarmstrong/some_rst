packages/lending/src/views/dashboard/deposit/item.tsx
=====================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import React, { useMemo } from 'react';
import { hooks, utils, TokenIcon } from '@oyster/common';
import { UserDeposit } from '../../../hooks';
import { calculateDepositAPY } from '../../../models/lending';
import { Button } from 'antd';
import { Link } from 'react-router-dom';
import { LABELS } from '../../../constants';
const { useTokenName } = hooks;
const { formatNumber, formatPct } = utils;

export const DepositItem = (props: { userDeposit: UserDeposit }) => {
  const { reserve, info } = props.userDeposit;
  const mintAddress = reserve.info.liquidityMint;
  const name = useTokenName(mintAddress);

  const depositAPY = useMemo(() => calculateDepositAPY(reserve.info), [
    reserve,
  ]);

  return (
    <div className="dashboard-item">
      <span style={{ display: 'flex' }}>
        <TokenIcon mintAddress={mintAddress} />
        {name}
      </span>
      <div>
        <div>
          <div>
            <em>{formatNumber.format(info.amount)}</em> {name}
          </div>
          <div className="dashboard-amount-quote">
            ${formatNumber.format(info.amountInQuote)}
          </div>
        </div>
      </div>
      <div>{formatPct.format(depositAPY)}</div>
      <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
        <Link to={`/deposit/${reserve.pubkey.toBase58()}`}>
          <Button type="primary">
            <span>{LABELS.DEPOSIT_ACTION}</span>
          </Button>
        </Link>
        <Link to={`/withdraw/${reserve.pubkey.toBase58()}`}>
          <Button type="text">
            <span>{LABELS.WITHDRAW_ACTION}</span>
          </Button>
        </Link>
      </div>
    </div>
  );
};


