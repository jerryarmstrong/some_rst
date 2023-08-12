packages/common/src/components/BackButton/index.tsx
===================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import React from 'react';
import { Button } from 'antd';
import { LABELS } from '../../constants';
import { useHistory } from 'react-router-dom';

export const BackButton = () => {
  const history = useHistory();
  return (
    <Button type="text" onClick={history.goBack}>
      {LABELS.GO_BACK_ACTION}
    </Button>
  );
};


