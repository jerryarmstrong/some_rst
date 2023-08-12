packages/sdk/core/src/accounts/GovernanceAccount.ts
===================================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import * as models from './models/index';

/**
 * A union of possible account classes that are relevant to governance
 */
export type GovernanceAccount =
  | models.Governance
  | models.ProgramMetadata
  | models.Proposal
  | models.ProposalTransaction
  | models.Realm
  | models.RealmConfig
  | models.SignatoryRecord
  | models.TokenOwnerRecord
  | models.VoteRecord;


