hub/components/FeedItemComment/gql.ts
=====================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import * as IT from 'io-ts';
import { gql } from 'urql';

import { feedItemComment, FeedItemComment } from '../FeedItem/gql';

export const getComments = gql`
  ${feedItemComment}

  query getComment(
    $commentId: RealmFeedItemCommentID!
    $feedItemId: RealmFeedItemID!
  ) {
    feedItemComment(commentId: $commentId, feedItemId: $feedItemId, depth: 6) {
      ...Comment
      replies {
        ...Comment
        replies {
          ...Comment
          replies {
            ...Comment
            replies {
              ...Comment
              replies {
                ...Comment
                replies {
                  ...Comment
                  replies {
                    ...Comment
                  }
                }
              }
            }
          }
        }
      }
    }
  }
`;

export const getCommentResp = IT.type({
  feedItemComment: FeedItemComment,
});


