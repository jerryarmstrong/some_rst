js/packages/common/src/components/BackButton/index.tsx
======================================================

Last edited: 2022-06-29 06:18:54

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


