examples/xnft/prices/src/App/_helpers/getChartDataTime.ts
=========================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import { ChartType } from "../_types/ChartType";

export const getChartDataTime = (chart: ChartType) =>
  ["1H", "1D"].includes(chart)
    ? "minute"
    : ["1W", "1M"].includes(chart)
    ? "hour"
    : "day";


