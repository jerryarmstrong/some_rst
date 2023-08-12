src/validators/index.ts
=======================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: ts

    /* eslint-disable @typescript-eslint/no-redeclare */

import { type, any, Infer, string } from "superstruct";

export type ParsedInfo = Infer<typeof ParsedInfo>;
export const ParsedInfo = type({
  type: string(),
  info: any(),
});


