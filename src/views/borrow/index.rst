src/views/borrow/index.tsx
==========================

Last edited: 2021-03-16 20:45:52

Contents:

.. code-block:: tsx

    import { Card } from "antd";
import React from "react";
import { LABELS } from "../../constants";
import { useLendingReserves } from "../../hooks";
import { BorrowItem } from "./item";
import "./itemStyle.less";

export const BorrowView = () => {
  const { reserveAccounts } = useLendingReserves();
  return (
    <div className="flexColumn">
      <Card>
        <div className="borrow-item deposit-header">
          <div>{LABELS.TABLE_TITLE_ASSET}</div>
          <div>Serum Dex Price</div>
          <div>{LABELS.TABLE_TITLE_MAX_BORROW}</div>
          <div>{LABELS.TABLE_TITLE_APY}</div>
          <div></div>
        </div>
        {reserveAccounts.map((account) => (
          <BorrowItem
            key={account.pubkey.toBase58()}
            reserve={account.info}
            address={account.pubkey}
          />
        ))}
      </Card>
    </div>
  );
};


