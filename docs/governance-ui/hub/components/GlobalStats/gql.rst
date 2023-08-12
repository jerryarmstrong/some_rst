hub/components/GlobalStats/gql.ts
=================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import * as IT from 'io-ts';
import { gql } from 'urql';

import { PublicKey } from '@hub/types/decoders/PublicKey';

export const getPerms = gql`
  query {
    me {
      amSiteAdmin
      publicKey
    }
  }
`;

export const getPermsResp = IT.type({
  me: IT.union([
    IT.null,
    IT.type({
      amSiteAdmin: IT.union([IT.null, IT.boolean]),
      publicKey: PublicKey,
    }),
  ]),
});


