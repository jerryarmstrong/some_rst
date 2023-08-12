clients/js/src/revisions/v1/any.ts
==================================

Last edited: 2023-08-01 17:12:05

Contents:

.. code-block:: ts

    import type { RuleV2 } from '../v2';
import { RuleV1, isRuleV1 } from './rule';

export type AnyRuleV1 = {
  Any: {
    rules: RuleV1[];
  };
};

export const isAnyRuleV1 = (rule: RuleV1 | RuleV2): rule is AnyRuleV1 =>
  isRuleV1(rule) && 'Any' in (rule as object);


