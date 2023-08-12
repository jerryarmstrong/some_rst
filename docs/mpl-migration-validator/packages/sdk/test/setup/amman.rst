packages/sdk/test/setup/amman.ts
================================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: ts

    import { Amman } from '@metaplex-foundation/amman-client';
import { cusper } from '../utils/errors';

import { PROGRAM_ADDRESS } from '../../src/generated';
import { logDebug } from '.';

export const amman = Amman.instance({
  knownLabels: { [PROGRAM_ADDRESS]: 'Migration Validator Program' },
  log: logDebug,
  errorResolver: cusper,
});


