packages/bridge/src/components/SecurityAuditButton/index.tsx
============================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import React from 'react';
import { Button } from 'antd';

import './index.less';

export const SecurityAuditButton = () => {
  return (
    <Button
      className={'audit-button'}
      target={'_blank'}
      href={'https://github.com/certusone/wormhole'}
    >
      Security Audit
    </Button>
  );
};


