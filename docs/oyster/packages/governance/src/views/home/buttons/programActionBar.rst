packages/governance/src/views/home/buttons/programActionBar.tsx
===============================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import { Button, Popover, Space } from 'antd';
import React, { useRef } from 'react';

import { MoreOutlined } from '@ant-design/icons';
import { RegisterRealmButton } from './registerRealmButton';
import { UpdateProgramMetadataButton } from './updateProgramMetadataButton';

export function ProgramActionBar() {
  const parentRef = useRef<HTMLDivElement>(null);

  return (
    <div className="proposals-action-bar">
      <Space>
        <RegisterRealmButton
          buttonProps={{ style: { marginLeft: 'auto', marginRight: 0 } }}
        />
        <div ref={parentRef} className="realm-popup-action-container">
          <Popover
            title="Program Options"
            placement="bottomRight"
            arrowPointAtCenter
            trigger="click"
            getPopupContainer={() => parentRef.current!}
            content={
              <Space direction="vertical">
                <UpdateProgramMetadataButton></UpdateProgramMetadataButton>
              </Space>
            }
          >
            <Button style={{ paddingLeft: 8, paddingRight: 8 }}>
              <MoreOutlined rotate={90} />
            </Button>
          </Popover>
        </div>
      </Space>
    </div>
  );
}


