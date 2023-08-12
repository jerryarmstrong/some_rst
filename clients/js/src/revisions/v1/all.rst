clients/js/src/revisions/v1/all.ts
==================================

Last edited: 2023-08-01 17:12:05

Contents:

.. code-block:: ts

    import type { RuleV2 } from '../v2';
import { RuleV1, isRuleV1 } from './rule';

export type AllRuleV1 = {
  All: {
    rules: RuleV1[];
  };
};

export const isAllRuleV1 = (rule: RuleV1 | RuleV2): rule is AllRuleV1 =>
  isRuleV1(rule) && 'All' in (rule as object);


