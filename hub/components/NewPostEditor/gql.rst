hub/components/NewPostEditor/gql.ts
===================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import * as IT from 'io-ts';
import { gql } from 'urql';

import { feedItemPostParts, FeedItemPost } from '@hub/components/Home/Feed/gql';
import { PublicKey } from '@hub/types/decoders/PublicKey';

export const createPost = gql`
  mutation submitPost(
    $realm: PublicKey!
    $title: String!
    $document: RichTextDocument!
    $crosspostTo: [PublicKey!]
  ) {
    createPost(document: $document, realm: $realm, title: $title, crosspostTo: $crosspostTo) {
      ${feedItemPostParts}
    }
  }
`;

export const getRealmsList = gql`
  query realmDropdownList {
    realmDropdownList {
      name
      publicKey
      iconUrl
    }
  }
`;

export const createPostResp = IT.type({
  createPost: FeedItemPost,
});

export const getRealmsListResp = IT.type({
  realmDropdownList: IT.array(
    IT.type({
      name: IT.string,
      publicKey: PublicKey,
      iconUrl: IT.union([IT.null, IT.string]),
    }),
  ),
});


