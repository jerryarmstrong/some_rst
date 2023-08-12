hub/types/decoders/FeedItemCommentVoteType.ts
=============================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import * as IT from 'io-ts';

import { FeedItemCommentVoteType as _FeedItemCommentVoteType } from '../FeedItemCommentVoteType';

export const FeedItemCommentVoteTypeApprove = IT.literal(
  _FeedItemCommentVoteType.Approve,
);
export const FeedItemCommentVoteTypeDisapprove = IT.literal(
  _FeedItemCommentVoteType.Disapprove,
);

export const FeedItemCommentVoteType = IT.union([
  FeedItemCommentVoteTypeApprove,
  FeedItemCommentVoteTypeDisapprove,
]);


