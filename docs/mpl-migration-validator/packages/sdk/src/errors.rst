packages/sdk/src/errors.ts
==========================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: ts

    import { initCusper } from '@metaplex-foundation/cusper';
// @ts-ignore
import { errorFromCode } from './generated';

export const cusper = initCusper(errorFromCode);


