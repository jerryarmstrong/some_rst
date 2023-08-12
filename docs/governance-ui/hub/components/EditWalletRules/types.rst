hub/components/EditWalletRules/types.ts
=======================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import { TypeOf } from 'io-ts';

import * as gql from './gql';

export type Rules = TypeOf<
  typeof gql.getGovernanceRulesResp
>['realmByUrlId']['governance'];
export type CommunityRules = Rules['communityTokenRules'];
export type CouncilRules = Rules['councilTokenRules'];


