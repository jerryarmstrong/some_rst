hub/components/EditWalletRules/types.ts
=======================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import { TypeOf } from 'io-ts';

import * as gql from './gql';

export type Rules = TypeOf<
  typeof gql.getGovernanceRulesResp
>['realmByUrlId']['governance'];
export type CommunityRules = Rules['communityTokenRules'];
export type CouncilRules = Rules['councilTokenRules'];


