packages/bridge/src/views/proof-of-assets/index.tsx
===================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import React from 'react';

import './index.less';
import { AssetsTable } from '../../components/AssetsTable';

export const ProofOfAssetsView = () => {
  return (
    <div
      className="flexColumn transfer-bg"
      style={{ flex: 1, minHeight: '90vh' }}
    >
      <AssetsTable />
    </div>
  );
};


