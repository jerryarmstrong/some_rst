clients/js/src/revisions/v2/ruleHeader.ts
=========================================

Last edited: 2023-08-01 17:12:05

Contents:

.. code-block:: ts

    import {
  Serializer,
  mergeBytes,
  struct,
  u32,
} from '@metaplex-foundation/umi/serializers';
import { RuleTypeV2, getRuleTypeV2AsString } from './ruleType';

export type RuleHeaderV2 = { type: number; length: number };

export const getRuleHeaderV2Serializer = (): Serializer<RuleHeaderV2> =>
  struct([
    ['type', u32()],
    ['length', u32()],
  ]);

export const wrapSerializerInRuleHeaderV2 = <T extends { type: string }>(
  type: RuleTypeV2,
  serializer: Serializer<Omit<T, 'type'>>
): Serializer<T> => {
  const typeAsString = getRuleTypeV2AsString(type);
  const headerSerializer = getRuleHeaderV2Serializer();
  return {
    description: typeAsString,
    fixedSize: serializer.fixedSize === null ? null : serializer.fixedSize + 8,
    maxSize: serializer.maxSize === null ? null : serializer.maxSize + 8,
    serialize: (rule: T): Uint8Array => {
      const serializedRule = serializer.serialize(rule);
      const serializedHeader = headerSerializer.serialize({
        type,
        length: serializedRule.length,
      });
      return mergeBytes([serializedHeader, serializedRule]);
    },
    deserialize: (buffer: Uint8Array, offset = 0): [T, number] => {
      const [header] = headerSerializer.deserialize(buffer, offset);
      offset += 8;
      const slice = buffer.slice(offset, offset + header.length);
      const [rule] = serializer.deserialize(slice);
      return [{ ...rule, type: typeAsString } as T, offset + header.length];
    },
  };
};


