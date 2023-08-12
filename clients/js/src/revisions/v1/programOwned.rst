clients/js/src/revisions/v1/programOwned.ts
===========================================

Last edited: 2023-08-01 17:12:05

Contents:

.. code-block:: ts

    import type { RuleV2 } from '../v2';
import { RuleV1, isRuleV1 } from './rule';
import type { PublicKeyAsArrayOfBytes } from './publicKey';

export type ProgramOwnedRuleV1 = {
  ProgramOwned: {
    program: PublicKeyAsArrayOfBytes;
    field: string;
  };
};

export const isProgramOwnedRuleV1 = (
  rule: RuleV1 | RuleV2
): rule is ProgramOwnedRuleV1 =>
  isRuleV1(rule) && 'ProgramOwned' in (rule as object);


