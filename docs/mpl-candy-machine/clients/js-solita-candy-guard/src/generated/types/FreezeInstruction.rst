clients/js-solita-candy-guard/src/generated/types/FreezeInstruction.ts
======================================================================

Last edited: 2023-08-11 23:25:39

Contents:

.. code-block:: ts

    /**
 * This code was GENERATED using the solita package.
 * Please DO NOT EDIT THIS FILE, instead rerun solita to update it or write a wrapper to add functionality.
 *
 * See: https://github.com/metaplex-foundation/solita
 */

import * as beet from '@metaplex-foundation/beet';
/**
 * @category enums
 * @category generated
 */
export enum FreezeInstruction {
  Initialize,
  Thaw,
  UnlockFunds,
}

/**
 * @category userTypes
 * @category generated
 */
export const freezeInstructionBeet = beet.fixedScalarEnum(FreezeInstruction) as beet.FixedSizeBeet<
  FreezeInstruction,
  FreezeInstruction
>;


