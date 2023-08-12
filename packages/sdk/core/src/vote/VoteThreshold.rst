packages/sdk/core/src/vote/VoteThreshold.ts
===========================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import { VoteThresholdType } from './VoteThresholdType';

export class VoteThreshold {
  type: VoteThresholdType;
  value: number | undefined;

  constructor(args: { type: VoteThresholdType; value?: number | undefined }) {
    this.type = args.type;
    this.value = args.value;
  }
}


