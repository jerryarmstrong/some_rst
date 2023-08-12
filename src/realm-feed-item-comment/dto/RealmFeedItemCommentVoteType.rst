src/realm-feed-item-comment/dto/RealmFeedItemCommentVoteType.ts
===============================================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { registerEnumType } from '@nestjs/graphql';

/**
 * A vote for a comment, affecting the comment's score
 */
export enum RealmFeedItemCommentVoteType {
  Approve = 'Approve',
  Disapprove = 'Disapprove',
}

registerEnumType(RealmFeedItemCommentVoteType, {
  name: 'RealmFeedItemCommentVoteType',
  description: 'A vote on a comment',
  valuesMap: {
    [RealmFeedItemCommentVoteType.Approve]: {
      description: 'The comment was approved',
    },
    [RealmFeedItemCommentVoteType.Disapprove]: {
      description: 'The comment was disapproved',
    },
  },
});


