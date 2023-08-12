hub/components/DiscoverPage/Sidebar/Trending/Org/gql.ts
=======================================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import * as IT from 'io-ts';
import { gql } from 'urql';

export const getRealm = gql`
  query getRealm($realm: PublicKey!) {
    hub(realm: $realm) {
      twitterFollowerCount
    }
    realm(publicKey: $realm) {
      twitterHandle
    }
  }
`;

export const getRealmResp = IT.type({
  hub: IT.type({
    twitterFollowerCount: IT.number,
  }),
  realm: IT.type({
    twitterHandle: IT.union([IT.null, IT.string]),
  }),
});


