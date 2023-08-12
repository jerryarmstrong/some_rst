clients/js/src/revisions/v1/additionalSigner.ts
===============================================

Last edited: 2023-08-01 17:12:05

Contents:

.. code-block:: ts

    import type { RuleV2 } from '../v2';
import { PublicKeyAsArrayOfBytes } from './publicKey';
import { RuleV1, isRuleV1 } from './rule';

export type AdditionalSignerRuleV1 = {
  AdditionalSigner: {
    account: PublicKeyAsArrayOfBytes;
  };
};

export const isAdditionalSignerRuleV1 = (
  rule: RuleV1 | RuleV2
): rule is AdditionalSignerRuleV1 =>
  isRuleV1(rule) && 'AdditionalSigner' in (rule as object);


