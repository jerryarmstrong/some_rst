app/components/common/BalanceDelta.tsx
======================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { SolBalance } from '@components/common/SolBalance';
import { BigNumber } from 'bignumber.js';
import React from 'react';

export function BalanceDelta({ delta, isSol = false }: { delta: BigNumber; isSol?: boolean }) {
    let sols;

    if (isSol) {
        sols = <SolBalance lamports={Math.abs(delta.toNumber())} />;
    }

    if (delta.gt(0)) {
        return <span className="badge bg-success-soft">+{isSol ? sols : delta.toString()}</span>;
    } else if (delta.lt(0)) {
        return <span className="badge bg-warning-soft">{isSol ? <>-{sols}</> : delta.toString()}</span>;
    }

    return <span className="badge bg-secondary-soft">0</span>;
}


