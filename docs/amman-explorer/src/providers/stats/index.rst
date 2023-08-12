src/providers/stats/index.tsx
=============================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: tsx

    import React from "react";
import { SolanaClusterStatsProvider } from "./solanaClusterStats";

type Props = { children: React.ReactNode };
export function StatsProvider({ children }: Props) {
  return <SolanaClusterStatsProvider>{children}</SolanaClusterStatsProvider>;
}


