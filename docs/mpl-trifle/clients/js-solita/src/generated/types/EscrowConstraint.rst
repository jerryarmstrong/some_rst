clients/js-solita/src/generated/types/EscrowConstraint.ts
=========================================================

Last edited: 2023-07-13 14:48:42

Contents:

.. code-block:: ts

    /**
 * This code was GENERATED using the solita package.
 * Please DO NOT EDIT THIS FILE, instead rerun solita to update it or write a wrapper to add functionality.
 *
 * See: https://github.com/metaplex-foundation/solita
 */

import * as beet from '@metaplex-foundation/beet';
import { EscrowConstraintType, escrowConstraintTypeBeet } from './EscrowConstraintType';
export type EscrowConstraint = {
  tokenLimit: beet.bignum;
  constraintType: EscrowConstraintType;
  transferEffects: number;
};

/**
 * @category userTypes
 * @category generated
 */
export const escrowConstraintBeet = new beet.FixableBeetArgsStruct<EscrowConstraint>(
  [
    ['tokenLimit', beet.u64],
    ['constraintType', escrowConstraintTypeBeet],
    ['transferEffects', beet.u16],
  ],
  'EscrowConstraint',
);


