clients/js-solita/src/errors.ts
===============================

Last edited: 2023-08-01 17:12:05

Contents:

.. code-block:: ts

    import { initCusper } from '@metaplex-foundation/cusper';
// @ts-ignore
import { errorFromCode } from './generated';

export const cusper = initCusper(errorFromCode);


