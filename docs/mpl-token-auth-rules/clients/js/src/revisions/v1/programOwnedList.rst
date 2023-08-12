clients/js/src/revisions/v1/programOwnedList.ts
===============================================

Last edited: 2023-08-01 17:12:05

Contents:

.. code-block:: ts

    import type { RuleV2 } from '../v2';
import type { PublicKeyAsArrayOfBytes } from './publicKey';
import { RuleV1, isRuleV1 } from './rule';

export type ProgramOwnedListRuleV1 = {
  ProgramOwnedList: {
    programs: PublicKeyAsArrayOfBytes[];
    field: string;
  };
};

export const isProgramOwnedListRuleV1 = (
  rule: RuleV1 | RuleV2
): rule is ProgramOwnedListRuleV1 =>
  isRuleV1(rule) && 'ProgramOwnedList' in (rule as object);


