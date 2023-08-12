hub/hooks/useCluster.ts
=======================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import { useContext } from 'react';

import { ClusterType, context } from '@hub/providers/Cluster';

export function useCluster() {
  const value = useContext(context);
  return [value.cluster, value.setType, value.type] as const;
}

export { ClusterType };


