clients/js-solita-candy-machine-core/src/errors.ts
==================================================

Last edited: 2023-08-11 23:25:39

Contents:

.. code-block:: ts

    import { initCusper } from '@metaplex-foundation/cusper';
import { errorFromCode } from './generated';

export const cusper = initCusper(errorFromCode);


