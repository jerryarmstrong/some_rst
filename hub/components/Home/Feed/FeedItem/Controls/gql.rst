hub/components/Home/Feed/FeedItem/Controls/gql.ts
=================================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import * as IT from 'io-ts';
import { gql } from 'urql';

import { feedItemParts, FeedItem } from '../../gql';

export const toggleApproval = gql`
  ${feedItemParts}

  mutation toggleApproval($feedItemId: RealmFeedItemID!, $realm: PublicKey!) {
    voteOnFeedItem(feedItemId: $feedItemId, realm: $realm, vote: Approve) {
      ...FeedItemParts
    }
  }
`;

export const deletePost = gql`
  mutation($feedItemId: RealmFeedItemID!, $realm: PublicKey!) {
    deletePost(feedItemId: $feedItemId, realm: $realm)
  }
`;

export const toggleApprovalResp = IT.type({
  voteOnFeedItem: FeedItem,
});

export const deletePostResp = IT.type({
  deletePost: IT.boolean,
});


