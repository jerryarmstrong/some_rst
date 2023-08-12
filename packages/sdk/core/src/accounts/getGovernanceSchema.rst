packages/sdk/core/src/accounts/getGovernanceSchema.ts
=====================================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import { getGovernanceSchema as getProgramGovernanceSchema } from '../program/getGovernanceSchema';

import { AccountType } from './AccountType';

import { getProgramVersion } from './getProgramVersion';

/**
 * Returns the scheme for an account type
 */
export function getGovernanceSchema(accountType: AccountType) {
  return getProgramGovernanceSchema(getProgramVersion(accountType));
}


