clients/js/src/revisions/v2/additionalSigner.ts
===============================================

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
  struct,
} from '@metaplex-foundation/umi/serializers';
import type { RuleV1 } from '../v1';
import { RuleV2, isRuleV2 } from './rule';
import { wrapSerializerInRuleHeaderV2 } from './ruleHeader';
import { RuleTypeV2 } from './ruleType';

export type AdditionalSignerRuleV2 = {
  type: 'AdditionalSigner';
  publicKey: PublicKey;
};

export const additionalSignerV2 = (
  publicKey: PublicKeyInput
): AdditionalSignerRuleV2 => ({
  type: 'AdditionalSigner',
  publicKey: toPublicKey(publicKey),
});

export const getAdditionalSignerRuleV2Serializer =
  (): Serializer<AdditionalSignerRuleV2> =>
    wrapSerializerInRuleHeaderV2(
      RuleTypeV2.AdditionalSigner,
      struct([['publicKey', publicKeySerializer()]])
    );

export const isAdditionalSignerRuleV2 = (
  rule: RuleV1 | RuleV2
): rule is AdditionalSignerRuleV2 =>
  isRuleV2(rule) && rule.type === 'AdditionalSigner';


