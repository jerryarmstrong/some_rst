packages/sdk/core/src/vote/VoteType.ts
======================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import { VoteTypeKind } from './VoteTypeKind';

/**
 * Defines the type of voting, ie "single-choice", "multiple-choice"
 */
export class VoteType {
  type: VoteTypeKind;
  choiceCount: number | undefined;

  constructor(args: { type: VoteTypeKind; choiceCount: number | undefined }) {
    this.type = args.type;
    this.choiceCount = args.choiceCount;
  }

  static SINGLE_CHOICE = new VoteType({
    type: VoteTypeKind.SingleChoice,
    choiceCount: undefined,
  });

  static MULTI_CHOICE = (choiceCount: number) =>
    new VoteType({
      type: VoteTypeKind.MultiChoice,
      choiceCount: choiceCount,
    });

  isSingleChoice() {
    return this.type === VoteTypeKind.SingleChoice;
  }
}


