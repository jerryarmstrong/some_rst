clients/js/src/revisions/v1/pass.ts
===================================

Last edited: 2023-08-01 17:12:05

Contents:

.. code-block:: ts

    import type { RuleV2 } from '../v2';
import { RuleV1, isRuleV1 } from './rule';

export type PassRuleV1 = 'Pass';

export const isPassRuleV1 = (rule: RuleV1 | RuleV2): rule is PassRuleV1 =>
  isRuleV1(rule) && rule === 'Pass';


