src/components/RiskSlider/index.tsx
===================================

Last edited: 2021-03-16 20:45:52

Contents:

.. code-block:: tsx

    import { riskMarks } from "../../constants";
import { Slider } from "antd";
import React from "react";
import "./style.less";

export const RiskSlider = (props: {
  value: number;
  onChange: (val: number) => void;
}) => {
  return (
    <Slider
      onChange={props.onChange}
      className="risk-slider"
      marks={riskMarks}
      value={props.value}
    />
  );
};


