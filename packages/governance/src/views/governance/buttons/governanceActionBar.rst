packages/governance/src/views/governance/buttons/governanceActionBar.tsx
========================================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import { Button, Popover, Space } from 'antd';
import React, { useRef } from 'react';
import { Governance, Realm } from '@solana/spl-governance';

import { MoreOutlined } from '@ant-design/icons';
import { NewProposalButton } from './newProposalButton';
import { CreateNativeTreasuryButton } from './addNativeTreasuryButton';
import { ProgramAccount } from '@solana/spl-governance';

export function GovernanceActionBar({
  realm,
  governance,
}: {
  realm: ProgramAccount<Realm> | undefined;
  governance: ProgramAccount<Governance> | undefined;
}) {
  const parentRef = useRef<HTMLDivElement>(null);

  if (!realm) {
    return null;
  }

  return (
    <div className="proposals-action-bar">
      <Space>
        <NewProposalButton governance={governance} realm={realm} />
        <div ref={parentRef} className="realm-popup-action-container">
          <Popover
            title="Governance Options"
            placement="bottomRight"
            arrowPointAtCenter
            trigger="click"
            getPopupContainer={() => parentRef.current!}
            content={
              <Space direction="vertical">
                <CreateNativeTreasuryButton
                  realm={realm}
                  governance={governance}
                ></CreateNativeTreasuryButton>
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


