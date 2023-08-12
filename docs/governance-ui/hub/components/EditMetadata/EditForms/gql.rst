hub/components/EditMetadata/EditForms/gql.ts
============================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import * as IT from 'io-ts';
import { gql } from 'urql';

export const checkSymbol = gql`
  query checkSymbol($realm: PublicKey!, $symbol: String!) {
    canAssignSymbolToRealm(realm: $realm, symbol: $symbol)
  }
`;

export const checkSymbolResp = IT.type({
  canAssignSymbolToRealm: IT.boolean,
});


