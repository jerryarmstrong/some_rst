examples/xnft/prices/src/App/_types/ChartType.ts
================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import { Infer, enums } from "superstruct";

export type ChartType = Infer<typeof ChartType>;
export const ChartType = enums(["1H", "1D", "1W", "1M", "1Y", "ALL"]);


