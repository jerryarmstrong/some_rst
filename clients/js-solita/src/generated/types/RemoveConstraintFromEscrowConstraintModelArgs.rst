clients/js-solita/src/generated/types/RemoveConstraintFromEscrowConstraintModelArgs.ts
======================================================================================

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
export type RemoveConstraintFromEscrowConstraintModelArgs = {
  constraintName: string;
};

/**
 * @category userTypes
 * @category generated
 */
export const removeConstraintFromEscrowConstraintModelArgsBeet =
  new beet.FixableBeetArgsStruct<RemoveConstraintFromEscrowConstraintModelArgs>(
    [['constraintName', beet.utf8String]],
    'RemoveConstraintFromEscrowConstraintModelArgs',
  );


