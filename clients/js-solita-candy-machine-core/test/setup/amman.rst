clients/js-solita-candy-machine-core/test/setup/amman.ts
========================================================

Last edited: 2023-08-11 23:25:39

Contents:

.. code-block:: ts

    import { Amman } from '@metaplex-foundation/amman-client';
import { cusper } from '../utils/errors';

import { PROGRAM_ADDRESS } from '../../src/generated';
import { logDebug } from '.';

export const amman = Amman.instance({
  knownLabels: { [PROGRAM_ADDRESS]: 'Candy Machine Core' },
  log: logDebug,
  errorResolver: cusper,
});


