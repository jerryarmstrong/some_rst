clients/js/src/revisions/v1/amount.ts
=====================================

Last edited: 2023-08-01 17:12:05

Contents:

.. code-block:: ts

    import type { AmountOperator } from '../shared';
import type { RuleV2 } from '../v2';
import { RuleV1, isRuleV1 } from './rule';

export type AmountRuleV1 = {
  Amount: {
    amount: number;
    operator: AmountOperator;
    field: string;
  };
};

export const isAmountRuleV1 = (rule: RuleV1 | RuleV2): rule is AmountRuleV1 =>
  isRuleV1(rule) && 'Amount' in (rule as object);


