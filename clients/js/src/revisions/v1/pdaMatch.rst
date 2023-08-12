clients/js/src/revisions/v1/pdaMatch.ts
=======================================

Last edited: 2023-08-01 17:12:05

Contents:

.. code-block:: ts

    import type { RuleV2 } from '../v2';
import { RuleV1, isRuleV1 } from './rule';
import type { PublicKeyAsArrayOfBytes } from './publicKey';

export type PdaMatchRuleV1 = {
  PDAMatch: {
    program: PublicKeyAsArrayOfBytes;
    pda_field: string;
    seeds_field: string;
  };
};

export const isPdaMatchRuleV1 = (
  rule: RuleV1 | RuleV2
): rule is PdaMatchRuleV1 => isRuleV1(rule) && 'PDAMatch' in (rule as object);


