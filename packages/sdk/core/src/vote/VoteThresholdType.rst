packages/sdk/core/src/vote/VoteThresholdType.ts
===============================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    export enum VoteThresholdType {
  // Approval Quorum
  YesVotePercentage = 0,
  // Not supported in the current version
  QuorumPercentage = 1,
  // Supported for VERSION >= 3
  Disabled = 2,
}


