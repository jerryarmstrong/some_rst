clients/js/test/revisions/v1/amount.test.ts
===========================================

Last edited: 2023-08-01 17:12:05

Contents:

.. code-block:: ts

    /* eslint-disable prefer-template */
import { generateSigner, publicKeyBytes } from '@metaplex-foundation/umi';
import test from 'ava';
import {
  AmountOperator,
  RuleSetRevisionV1,
  isAmountRuleV1,
} from '../../../src';
import { createUmiSync } from '../../_setup';

test('isAmountRuleV1', async (t) => {
  const umi = createUmiSync();
  const owner = generateSigner(umi).publicKey;

  const revision: RuleSetRevisionV1 = {
    libVersion: 1,
    ruleSetName: 'My Rule Set',
    owner: [...publicKeyBytes(owner)],
    operations: {
      deposit: {
        Amount: {
          amount: 100,
          operator: AmountOperator.Eq,
          field: 'amount',
        },
      },
    },
  };

  t.true(isAmountRuleV1(revision.operations.deposit));
});


