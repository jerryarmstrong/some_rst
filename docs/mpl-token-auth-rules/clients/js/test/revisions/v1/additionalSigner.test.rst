clients/js/test/revisions/v1/additionalSigner.test.ts
=====================================================

Last edited: 2023-08-01 17:12:05

Contents:

.. code-block:: ts

    /* eslint-disable prefer-template */
import { generateSigner, publicKeyBytes } from '@metaplex-foundation/umi';
import test from 'ava';
import { RuleSetRevisionV1, isAdditionalSignerRuleV1 } from '../../../src';
import { createUmiSync } from '../../_setup';

test('isAdditionalSigner', async (t) => {
  const umi = createUmiSync();
  const owner = generateSigner(umi).publicKey;
  const publicKeyA = generateSigner(umi).publicKey;
  const revision: RuleSetRevisionV1 = {
    libVersion: 1,
    ruleSetName: 'My Rule Set',
    owner: [...publicKeyBytes(owner)],
    operations: {
      deposit: {
        AdditionalSigner: {
          account: [...publicKeyBytes(publicKeyA)],
        },
      },
    },
  };

  t.true(isAdditionalSignerRuleV1(revision.operations.deposit));
});


