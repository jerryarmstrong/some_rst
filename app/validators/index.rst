app/validators/index.ts
=======================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: ts

    /* eslint-disable @typescript-eslint/no-redeclare */

import { any, Infer, string, type } from 'superstruct';

export type ParsedInfo = Infer<typeof ParsedInfo>;
export const ParsedInfo = type({
    info: any(),
    type: string(),
});


