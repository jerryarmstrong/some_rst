app/components/common/SolBalance.tsx
====================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { lamportsToSolString } from '@utils/index';
import React from 'react';

export function SolBalance({
    lamports,
    maximumFractionDigits = 9,
}: {
    lamports: number | bigint;
    maximumFractionDigits?: number;
}) {
    return (
        <span>
            ◎<span className="font-monospace">{lamportsToSolString(lamports, maximumFractionDigits)}</span>
        </span>
    );
}


