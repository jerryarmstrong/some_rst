clients/js/test/revisions/v2/additionalSigner.test.ts
=====================================================

Last edited: 2023-08-01 17:12:05

Contents:

.. code-block:: ts

    /* eslint-disable prefer-template */
import { generateSigner } from '@metaplex-foundation/umi';
import test from 'ava';
import { additionalSignerV2 } from '../../../src';
import {
  createUmiSync,
  deserializeRuleV2FromHex,
  serializeRuleV2AsHex,
  toHex,
} from '../../_setup';

test('serialize', async (t) => {
  const umi = createUmiSync();
  const { publicKey } = generateSigner(umi);
  const rule = additionalSignerV2(publicKey);
  const serializedRule = serializeRuleV2AsHex(rule);
  t.is(
    serializedRule,
    '01000000' + // Rule type
      '20000000' + // Rule length
      toHex(publicKey) // Additional signer
  );
});

test('deserialize', async (t) => {
  const umi = createUmiSync();
  const { publicKey } = generateSigner(umi);
  const buffer =
    '01000000' + // Rule type
    '20000000' + // Rule length
    toHex(publicKey); // Additional signer
  const rule = deserializeRuleV2FromHex(buffer);
  t.deepEqual(rule, additionalSignerV2(publicKey));
});


