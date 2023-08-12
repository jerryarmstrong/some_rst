hydra/js/test/setup/amman.ts
============================

Last edited: 2023-07-31 23:00:16

Contents:

.. code-block:: ts

    import { Amman } from '@metaplex-foundation/amman-client';
import { cusper } from '../utils/errors';

import { PROGRAM_ADDRESS } from '../../src/generated';
import { logDebug } from '.';

export const amman = Amman.instance({
  knownLabels: { [PROGRAM_ADDRESS]: 'Hydra' },
  log: logDebug,
  errorResolver: cusper,
});


