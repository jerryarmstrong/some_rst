packages/gumdrop/src/components/DefaultModal/index.tsx
======================================================

Last edited: 2022-08-25 19:21:42

Contents:

.. code-block:: tsx

    import React from 'react';
import { Modal } from 'antd';

import './index.css';

export const DefaultModal = (props: any) => {
  const { children, bodyStyle, width, ...rest } = props;

  return (
    <Modal
      style={{ background: 'transparent', borderRadius: 16 }}
      bodyStyle={{
        background: '#333333',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        ...bodyStyle,
      }}
      footer={null}
      width={width || 400}
      {...rest}
    >
      {children}
    </Modal>
  );
};


