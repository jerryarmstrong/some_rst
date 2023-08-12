js/packages/common/src/components/MetaplexOverlay/index.tsx
===========================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: tsx

    import React from 'react';
import { Modal } from 'antd';

export const MetaplexOverlay = (props: any) => {
  const { children, ...rest } = props;

  const content = (
    <div
      style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        pointerEvents: 'auto',
        justifyContent: 'center',
      }}
    >
      {children}
    </div>
  );

  return (
    <Modal
      centered
      modalRender={() => content}
      width={'100vw'}
      mask={false}
      {...rest}
    ></Modal>
  );
};


