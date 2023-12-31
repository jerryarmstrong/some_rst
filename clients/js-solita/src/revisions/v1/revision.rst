clients/js-solita/src/revisions/v1/revision.ts
==============================================

Last edited: 2023-08-01 17:12:05

Contents:

.. code-block:: ts

    import { encode, decode } from '@msgpack/msgpack';
import type { PublicKeyAsArrayOfBytes } from './publicKey';
import type { RuleV1 } from './rule';

export type RuleSetRevisionV1 = {
  /** The version of the ruleset. */
  libVersion: 1;
  /** The name of the ruleset. */
  ruleSetName: string;
  /** The owner of the ruleset as an array of 32 bytes. */
  owner: PublicKeyAsArrayOfBytes;
  /** The operations of the ruleset. */
  operations: Record<string, RuleV1>;
};

export const serializeRuleSetRevisionV1 = (ruleSet: RuleSetRevisionV1): Buffer => {
  return Buffer.from(encode(ruleSet));
};

export const deserializeRuleSetRevisionV1 = (buffer: Buffer, offset = 0): RuleSetRevisionV1 => {
  const ruleSet = decode(buffer.subarray(offset + 1));

  if (Array.isArray(ruleSet)) {
    return {
      libVersion: ruleSet[0],
      owner: ruleSet[1],
      ruleSetName: ruleSet[2],
      operations: ruleSet[3],
    };
  }

  return ruleSet as RuleSetRevisionV1;
};


