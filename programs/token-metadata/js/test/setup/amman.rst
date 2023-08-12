programs/token-metadata/js/test/setup/amman.ts
==============================================

Last edited: 2023-08-11 07:39:15

Contents:

.. code-block:: ts

    import { Amman } from '@metaplex-foundation/amman-client';
import { cusper } from '../utils/errors';

import { PROGRAM_ADDRESS } from '../../src/generated';
import { logDebug } from '.';

export const amman = Amman.instance({
  knownLabels: { [PROGRAM_ADDRESS]: 'Token Metadata Program' },
  log: logDebug,
  errorResolver: cusper,
});


