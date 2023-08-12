examples/xnft/prices/src/App/_types/GraphDataPointType.ts
=========================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import { Infer, number, tuple } from "superstruct";

export type GraphDataPointType = Infer<typeof GraphDataPointType>;
export const GraphDataPointType = tuple([number(), number()]);


