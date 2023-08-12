clients/js/src/revisions/v1/pubkeyMatch.ts
==========================================

Last edited: 2023-08-01 17:12:05

Contents:

.. code-block:: ts

    import type { RuleV2 } from '../v2';
import type { PublicKeyAsArrayOfBytes } from './publicKey';
import { RuleV1, isRuleV1 } from './rule';

export type PubkeyMatchRuleV1 = {
  PubkeyMatch: {
    pubkey: PublicKeyAsArrayOfBytes;
    field: string;
  };
};

export const isPubkeyMatchRuleV1 = (
  rule: RuleV1 | RuleV2
): rule is PubkeyMatchRuleV1 =>
  isRuleV1(rule) && 'PubkeyMatch' in (rule as object);


