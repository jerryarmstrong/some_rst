src/components/Icons/info.tsx
=============================

Last edited: 2021-03-16 20:45:52

Contents:

.. code-block:: tsx

    import { Button, Popover } from "antd";
import React from "react";

import { InfoCircleOutlined } from "@ant-design/icons";

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


