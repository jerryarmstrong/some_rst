clients/js-solita/test/_amman.ts
================================

Last edited: 2023-08-01 17:12:05

Contents:

.. code-block:: ts

    import { Amman } from '@metaplex-foundation/amman-client';
import { PROGRAM_ADDRESS } from '../src/generated';

export const amman = Amman.instance({
  knownLabels: { [PROGRAM_ADDRESS]: 'Token Auth Rules' },
  connectClient: false,
});


