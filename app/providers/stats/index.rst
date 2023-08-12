app/providers/stats/index.tsx
=============================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { SolanaPingProvider } from '@providers/stats/SolanaPingProvider';
import React from 'react';

import { SolanaClusterStatsProvider } from './solanaClusterStats';

type Props = { children: React.ReactNode };
export function StatsProvider({ children }: Props) {
    return (
        <SolanaClusterStatsProvider>
            <SolanaPingProvider>{children}</SolanaPingProvider>
        </SolanaClusterStatsProvider>
    );
}


