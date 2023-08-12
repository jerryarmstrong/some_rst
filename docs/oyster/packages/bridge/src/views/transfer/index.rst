packages/bridge/src/views/transfer/index.tsx
============================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import React from 'react';
import './index.less';
import { Transfer } from '../../components/Transfer';

export const TransferView = () => {
  return (
    <>
      <div
        className="flexColumn transfer-bg"
        style={{ flex: 1, minHeight: '90vh' }}
      >
        <Transfer />
      </div>
    </>
  );
};


