packages/lending/src/views/borrowReserve/index.tsx
==================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import React from "react";
import {
  useBorrowingPower,
  useLendingReserve,
  useUserObligations,
} from "../../hooks";
import { useParams } from "react-router-dom";
import "./style.less";

import { BorrowInput } from "../../components/BorrowInput";
import {
  SideReserveOverview,
  SideReserveOverviewMode,
} from "../../components/SideReserveOverview";
import { Card, Col, Row, Statistic } from "antd";
import { BarChartStatistic } from "../../components/BarChartStatistic";
import { GUTTER, LABELS } from "../../constants";

export const BorrowReserveView = () => {
  const { id } = useParams<{ id: string }>();
  const lendingReserve = useLendingReserve(id);
  const { userObligations, totalInQuote: loansValue } = useUserObligations();

  const { totalInQuote: borrowingPower, utilization } = useBorrowingPower(id);

  if (!lendingReserve) {
    return null;
  }

  return (
    <div className="borrow-reserve">
      <Row gutter={GUTTER}>
        <Col xs={24} xl={5}>
          <Card>
            <Statistic
              title={LABELS.BORROWED_VALUE}
              value={loansValue}
              precision={2}
              prefix="$"
            />
          </Card>
        </Col>
        <Col xs={24} xl={5}>
          <Card>
            <Statistic
              title={LABELS.BORROWING_POWER_USED}
              value={utilization * 100}
              precision={2}
              suffix="%"
            />
          </Card>
        </Col>
        <Col xs={24} xl={5}>
          <Card>
            <Statistic
              title={LABELS.BORROWING_POWER_VALUE}
              value={borrowingPower}
              valueStyle={{ color: "#3fBB00" }}
              precision={2}
              prefix="$"
            />
          </Card>
        </Col>
        <Col xs={24} xl={9}>
          <Card>
            <BarChartStatistic
              title="Your Loans"
              items={userObligations}
              getPct={(item) =>
                item.obligation.info.borrowedInQuote / loansValue
              }
              name={(item) => item.obligation.info.repayName}
            />
          </Card>
        </Col>
      </Row>
      <Row gutter={GUTTER} style={{ flex: 1 }}>
        <Col xs={24} xl={15}>
          <BorrowInput className="card-fill" reserve={lendingReserve} />
        </Col>
        <Col xs={24} xl={9}>
          <SideReserveOverview
            className="card-fill"
            reserve={lendingReserve}
            mode={SideReserveOverviewMode.Borrow}
          />
        </Col>
      </Row>
    </div>
  );
};


