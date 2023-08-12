packages/lending/src/contexts/pools.tsx
=======================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import React, { useContext, useMemo } from 'react';

import { PoolInfo } from '../models';

const AccountsContext = React.createContext<any>(null);

export function useCachedPool(legacy = false) {
  const context = useContext(AccountsContext);

  const allPools = context.pools as PoolInfo[];
  const pools = useMemo(() => {
    return allPools.filter((p) => p.legacy === legacy);
  }, [allPools, legacy]);

  return {
    pools,
  };
}


