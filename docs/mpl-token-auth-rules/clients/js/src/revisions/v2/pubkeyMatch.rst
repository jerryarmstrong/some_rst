clients/js/src/revisions/v2/pubkeyMatch.ts
==========================================

Last edited: 2023-08-01 17:12:05

Contents:

.. code-block:: ts

    import {
  PublicKey,
  PublicKeyInput,
  publicKey as toPublicKey,
} from '@metaplex-foundation/umi';
import {
  Serializer,
  publicKey as publicKeySerializer,
  string,
  struct,
} from '@metaplex-foundation/umi/serializers';
import type { RuleV1 } from '../v1';
import { RuleV2, isRuleV2 } from './rule';
import { wrapSerializerInRuleHeaderV2 } from './ruleHeader';
import { RuleTypeV2 } from './ruleType';

export type PubkeyMatchRuleV2 = {
  type: 'PubkeyMatch';
  field: string;
  publicKey: PublicKey;
};

export const pubkeyMatchV2 = (
  field: string,
  publicKey: PublicKeyInput
): PubkeyMatchRuleV2 => ({
  type: 'PubkeyMatch',
  publicKey: toPublicKey(publicKey),
  field,
});

export const getPubkeyMatchRuleV2Serializer =
  (): Serializer<PubkeyMatchRuleV2> =>
    wrapSerializerInRuleHeaderV2(
      RuleTypeV2.PubkeyMatch,
      struct([
        ['publicKey', publicKeySerializer()],
        ['field', string({ size: 32 })],
      ])
    );

export const isPubkeyMatchRuleV2 = (
  rule: RuleV1 | RuleV2
): rule is PubkeyMatchRuleV2 => isRuleV2(rule) && rule.type === 'PubkeyMatch';


