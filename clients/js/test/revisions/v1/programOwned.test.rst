clients/js/test/revisions/v1/programOwned.test.ts
=================================================

Last edited: 2023-08-01 17:12:05

Contents:

.. code-block:: ts

    /* eslint-disable prefer-template */
import { generateSigner, publicKeyBytes } from '@metaplex-foundation/umi';
import test from 'ava';
import { RuleSetRevisionV1, isProgramOwnedRuleV1 } from '../../../src';
import { createUmiSync } from '../../_setup';

test('isProgramOwnedV1', async (t) => {
  const umi = createUmiSync();
  const owner = generateSigner(umi).publicKey;
  const publicKeyA = generateSigner(umi).publicKey;

  const revision: RuleSetRevisionV1 = {
    libVersion: 1,
    ruleSetName: 'My Rule Set',
    owner: [...publicKeyBytes(owner)],
    operations: {
      deposit: {
        ProgramOwned: {
          field: 'myField',
          program: [...publicKeyBytes(publicKeyA)],
        },
      },
    },
  };

  t.true(isProgramOwnedRuleV1(revision.operations.deposit));
});


