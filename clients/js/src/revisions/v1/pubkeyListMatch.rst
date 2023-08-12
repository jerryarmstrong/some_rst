clients/js/src/revisions/v1/pubkeyListMatch.ts
==============================================

Last edited: 2023-08-01 17:12:05

Contents:

.. code-block:: ts

    import type { RuleV2 } from '../v2';
import type { PublicKeyAsArrayOfBytes } from './publicKey';
import { RuleV1, isRuleV1 } from './rule';

export type PubkeyListMatchRuleV1 = {
  PubkeyListMatch: {
    pubkeys: PublicKeyAsArrayOfBytes[];
    field: string;
  };
};
export const isPubkeyListMatchRuleV1 = (
  rule: RuleV1 | RuleV2
): rule is PubkeyListMatchRuleV1 =>
  isRuleV1(rule) && 'PubkeyListMatch' in (rule as object);


