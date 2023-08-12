packages/sdk/core/src/vote/VoteChoice.ts
========================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    export class VoteChoice {
  rank: number;
  weightPercentage: number;

  constructor(args: { rank: number; weightPercentage: number }) {
    this.rank = args.rank;
    this.weightPercentage = args.weightPercentage;
  }
}


