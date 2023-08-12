packages/common/src/components/Icons/info.tsx
=============================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import { Button, Popover } from 'antd';
import React from 'react';

import { InfoCircleOutlined } from '@ant-design/icons';

export const Info = (props: {
  text: React.ReactElement;
  style?: React.CSSProperties;
}) => {
  return (
    <Popover
      trigger="hover"
      content={<div style={{ width: 300 }}>{props.text}</div>}
    >
      <Button type="text" shape="circle">
        <InfoCircleOutlined style={props.style} />
      </Button>
    </Popover>
  );
};


