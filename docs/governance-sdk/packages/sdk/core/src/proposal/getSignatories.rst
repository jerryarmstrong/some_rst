packages/sdk/core/src/proposal/getSignatories.ts
================================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import type { Connection, PublicKey } from '@solana/web3.js';

import { getAccountsByFilters } from '../accounts/getAccountsByFilters';
import { SignatoryRecord } from '../accounts/models/SignatoryRecord';
import { createFilterFromPublicKey } from '../filters/createFilterFromPublicKey';

interface Args {
  connection: Connection;
  proposal: PublicKey;
  programId: PublicKey;
}

export async function getSignatories({ connection, programId, proposal }: Args) {
  const filter = createFilterFromPublicKey(1, proposal);

  return getAccountsByFilters({
    connection,
    programId,
    accountClass: SignatoryRecord,
    filters: [filter],
  });
}


