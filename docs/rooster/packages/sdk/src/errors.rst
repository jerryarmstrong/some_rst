packages/sdk/src/errors.ts
==========================

Last edited: 2023-08-01 14:25:31

Contents:

.. code-block:: ts

    import { initCusper } from '@metaplex-foundation/cusper';
// @ts-ignore
import { errorFromCode } from './generated';

export const cusper = initCusper(errorFromCode);


