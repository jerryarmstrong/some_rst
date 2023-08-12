hub/hooks/useCluster.ts
=======================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import { useContext } from 'react';

import { ClusterType, context } from '@hub/providers/Cluster';

export function useCluster() {
  const value = useContext(context);
  return [value.cluster, value.setType, value.type] as const;
}

export { ClusterType };


