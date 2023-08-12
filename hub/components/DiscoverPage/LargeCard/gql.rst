hub/components/DiscoverPage/LargeCard/gql.ts
============================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import * as IT from 'io-ts';
import { gql } from 'urql';

export const getRealm = gql`
  query getRealm($realm: PublicKey!) {
    hub(realm: $realm) {
      twitterFollowerCount
    }
  }
`;

export const getRealmResp = IT.type({
  hub: IT.type({
    twitterFollowerCount: IT.number,
  }),
});


