src/components/BackButton/index.tsx
===================================

Last edited: 2021-03-16 20:45:52

Contents:

.. code-block:: tsx

    import React from "react";
import { Button } from "antd";
import { LABELS } from "../../constants";
import { useHistory } from "react-router-dom";

export const BackButton = () => {
  const history = useHistory();
  return (
    <Button type="text" onClick={history.goBack}>
      {LABELS.GO_BACK_ACTION}
    </Button>
  );
};


