clients/js-solita/src/revisions/v2/isWallet.ts
==============================================

Last edited: 2023-08-01 17:12:05

Contents:

.. code-block:: ts

    import { deserializeString32, serializeString32 } from './helpers';
import { serializeRuleHeaderV2 } from './rule';
import { RuleTypeV2 } from './ruleType';

export type IsWalletRuleV2 = {
  type: 'IsWallet';
  field: string;
};

export const isWalletV2 = (field: string): IsWalletRuleV2 => ({ type: 'IsWallet', field });

export const serializeIsWalletV2 = (rule: IsWalletRuleV2): Buffer => {
  return Buffer.concat([
    serializeRuleHeaderV2(RuleTypeV2.IsWallet, 32),
    serializeString32(rule.field),
  ]);
};

export const deserializeIsWalletV2 = (buffer: Buffer, offset = 0): IsWalletRuleV2 => {
  offset += 8; // Skip rule header.
  const field = deserializeString32(buffer, offset);
  return isWalletV2(field);
};


