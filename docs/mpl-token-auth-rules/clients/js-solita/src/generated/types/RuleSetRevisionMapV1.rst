clients/js-solita/src/generated/types/RuleSetRevisionMapV1.ts
=============================================================

Last edited: 2023-08-01 17:12:05

Contents:

.. code-block:: ts

    /**
 * This code was GENERATED using the solita package.
 * Please DO NOT EDIT THIS FILE, instead rerun solita to update it or write a wrapper to add functionality.
 *
 * See: https://github.com/metaplex-foundation/solita
 */

import * as beet from '@metaplex-foundation/beet';
export type RuleSetRevisionMapV1 = {
  ruleSetRevisions: beet.bignum[];
};

/**
 * @category userTypes
 * @category generated
 */
export const ruleSetRevisionMapV1Beet = new beet.FixableBeetArgsStruct<RuleSetRevisionMapV1>(
  [['ruleSetRevisions', beet.array(beet.u64)]],
  'RuleSetRevisionMapV1',
);


