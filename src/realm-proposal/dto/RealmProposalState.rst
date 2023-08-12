src/realm-proposal/dto/RealmProposalState.ts
============================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { registerEnumType } from '@nestjs/graphql';

export enum RealmProposalState {
  Cancelled = 'Cancelled',
  Completed = 'Completed',
  Defeated = 'Defeated',
  Draft = 'Draft',
  Executable = 'Executable',
  ExecutingWithErrors = 'ExecutingWithErrors',
  Finalizing = 'Finalizing',
  SigningOff = 'SigningOff',
  Voting = 'Voting',
}

registerEnumType(RealmProposalState, {
  name: 'RealmProposalState',
  description: 'Current state of a proposal',
});


