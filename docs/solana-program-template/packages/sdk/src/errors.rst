packages/sdk/src/errors.ts
==========================

Last edited: 2023-04-22 23:05:55

Contents:

.. code-block:: ts

    import { initCusper } from '@metaplex-foundation/cusper';
// @ts-ignore
import { errorFromCode } from './generated';

export const cusper = initCusper(errorFromCode);


