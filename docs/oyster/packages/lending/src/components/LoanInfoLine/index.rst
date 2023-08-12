packages/lending/src/components/LoanInfoLine/index.tsx
======================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import { Card, Col, Row, Statistic } from 'antd';

import React, { useMemo } from 'react';
import { EnrichedLendingObligation, useLendingReserve } from '../../hooks';

import { calculateBorrowAPY, collateralToLiquidity } from '../../models';
import { GUTTER } from '../../constants';
import { hooks, contexts, utils } from '@oyster/common';
const { useTokenName } = hooks;
const { useMint } = contexts.Accounts;
const { formatNumber, formatPct, fromLamports, wadToLamports } = utils;
export const LoanInfoLine = (props: {
  className?: string;
  obligation: EnrichedLendingObligation;
}) => {
  const obligation = props.obligation;

  const repayReserve = useLendingReserve(obligation?.info.borrowReserve);
  const withdrawReserve = useLendingReserve(obligation?.info.collateralReserve);

  const liquidityMint = useMint(repayReserve?.info.liquidityMint);
  const collateralMint = useMint(withdrawReserve?.info.liquidityMint);
  const repayName = useTokenName(repayReserve?.info.liquidityMint);
  const withdrawName = useTokenName(withdrawReserve?.info.liquidityMint);

  const borrowAPY = useMemo(
    () => (repayReserve ? calculateBorrowAPY(repayReserve?.info) : 0),
    [repayReserve],
  );
  if (!obligation || !repayReserve) {
    return null;
  }
  const borrowAmount = fromLamports(
    wadToLamports(obligation?.info.borrowAmountWad),
    liquidityMint,
  );
  const collateralLamports = collateralToLiquidity(
    obligation?.info.depositedCollateral,
    repayReserve.info,
  );
  const collateral = fromLamports(collateralLamports, collateralMint);

  return (
    <Row gutter={GUTTER}>
      <Col xs={24} xl={5}>
        <Card className={props.className}>
          <Statistic
            title="Loan Balance"
            value={obligation.info.borrowedInQuote}
            formatter={val => (
              <div>
                <div>
                  <em>{formatNumber.format(borrowAmount)}</em> {repayName}
                </div>
                <div className="dashboard-amount-quote">
                  ${formatNumber.format(parseFloat(val.toString()))}
                </div>
              </div>
            )}
          />
        </Card>
      </Col>
      <Col xs={24} xl={5}>
        <Card className={props.className}>
          <Statistic
            title="Collateral"
            value={obligation.info.collateralInQuote}
            formatter={val => (
              <div>
                <div>
                  <em>{formatNumber.format(collateral)}</em> {withdrawName}
                </div>
                <div className="dashboard-amount-quote">
                  ${formatNumber.format(parseFloat(val.toString()))}
                </div>
              </div>
            )}
          />
        </Card>
      </Col>
      <Col xs={24} xl={5}>
        <Card className={props.className}>
          <Statistic title="APY" value={formatPct.format(borrowAPY)} />
        </Card>
      </Col>
      <Col xs={24} xl={9}>
        <Card className={props.className}>
          <Statistic
            title="Health Factor"
            value={obligation.info.health.toFixed(2)}
          />
        </Card>
      </Col>
    </Row>
  );
};


