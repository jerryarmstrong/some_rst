src/components/common/BalanceDelta.tsx
======================================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: tsx

    import React from "react";
import { BigNumber } from "bignumber.js";
import { SolBalance } from "utils";

export function BalanceDelta({
  delta,
  isSol = false,
}: {
  delta: BigNumber;
  isSol?: boolean;
}) {
  let sols;

  if (isSol) {
    sols = <SolBalance lamports={delta.toNumber()} />;
  }

  if (delta.gt(0)) {
    return (
      <span className="badge bg-success-soft">
        +{isSol ? sols : delta.toString()}
      </span>
    );
  } else if (delta.lt(0)) {
    return (
      <span className="badge bg-warning-soft">
        {isSol ? <>-{sols}</> : delta.toString()}
      </span>
    );
  }

  return <span className="badge bg-secondary-soft">0</span>;
}


