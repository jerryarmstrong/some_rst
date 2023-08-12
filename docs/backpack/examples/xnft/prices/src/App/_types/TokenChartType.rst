examples/xnft/prices/src/App/_types/TokenChartType.ts
=====================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import { Infer, array, object, nullable, type, optional } from "superstruct";
import { GraphDataPointType } from "./GraphDataPointType";
import { ChartType } from "./ChartType";

export type TokenChartType = Infer<typeof TokenChartType>;
export const TokenChartType = object({
  activeChart: optional(ChartType),
  minute: optional(array(GraphDataPointType)),
  hour: optional(array(GraphDataPointType)),
  day: optional(array(GraphDataPointType)),
});


