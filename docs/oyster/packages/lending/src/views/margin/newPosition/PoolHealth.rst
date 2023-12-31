packages/lending/src/views/margin/newPosition/PoolHealth.tsx
============================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import Card from "antd/lib/card";
import React from "react";
import { PoolPrice } from "../../../components/PoolPrice";
import { SupplyOverview } from "../../../components/SupplyOverview";
import { Position } from "./interfaces";
import { usePoolAndTradeInfoFrom } from "./utils";

export default function PoolHealth({ newPosition }: { newPosition: Position }) {
  const { pool } = usePoolAndTradeInfoFrom(newPosition);
  return (
    <Card className="new-position-item new-position-item-bottom-left">
      {!pool && <span>Choose a CCY to see exchange rate information.</span>}
      {pool && (
        <>
          <PoolPrice pool={pool} />
          <SupplyOverview pool={pool} />
        </>
      )}
    </Card>
  );
}


