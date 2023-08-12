packages/sdk/core/src/program/getGovernanceSchema.ts
====================================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import { ProgramVersion } from '../constants';

import * as schema from './schema';

export function getGovernanceSchema(programVersion: ProgramVersion) {
  switch (programVersion) {
    case 1:
      return schema.GOVERNANCE_SCHEMA_V1;
    default:
      return schema.GOVERNANCE_SCHEMA;
  }
}


