packages/metavinci/src/components/Settings/index.tsx
====================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import React from 'react';
import { Button, Select } from 'antd';
import { contexts, useWallet } from '@oyster/common';

const { ENDPOINTS, useConnectionConfig } = contexts.Connection;

export const Settings = () => {
  const { connected, disconnect } = useWallet();
  const { endpoint, setEndpoint } = useConnectionConfig();

  return (
    <>
      <div style={{ display: 'grid' }}>
        Network:{' '}
        <Select
          onSelect={setEndpoint}
          value={endpoint}
          style={{ marginBottom: 20 }}
        >
          {ENDPOINTS.map(({ name, endpoint }) => (
            <Select.Option value={endpoint} key={endpoint}>
              {name}
            </Select.Option>
          ))}
        </Select>
        {connected && (
          <Button type="primary" onClick={disconnect}>
            Disconnect
          </Button>
        )}
      </div>
    </>
  );
};


