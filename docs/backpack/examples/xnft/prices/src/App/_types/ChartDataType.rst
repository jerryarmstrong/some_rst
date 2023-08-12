examples/xnft/prices/src/App/_types/ChartDataType.ts
====================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import { array, Infer, type } from "superstruct";
import { GraphDataPointType } from "./GraphDataPointType";

export type ChartDataType = Infer<typeof ChartDataType>;
export const ChartDataType = type({
  prices: array(GraphDataPointType),
});


