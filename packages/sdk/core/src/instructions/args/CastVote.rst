packages/sdk/core/src/instructions/args/CastVote.ts
===================================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import { Vote } from '../../vote/Vote';
import { YesNoVote } from '../../vote/YesNoVote';
import { InstructionType } from '../InstructionType';

export class CastVote {
  instruction = InstructionType.CastVote;
  /**
   * The vote value
   * @deprecated
   */
  yesNoVote?: YesNoVote;
  /**
   * The vote value
   */
  vote?: Vote;

  constructor(args: { yesNoVote?: YesNoVote; vote?: Vote }) {
    this.yesNoVote = args.yesNoVote;
    this.vote = args.vote;
  }
}


