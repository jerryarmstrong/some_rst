nft-packs/js/src/generated/types/ClaimPackArgs.ts
=================================================

Last edited: 2023-07-31 23:00:16

Contents:

.. code-block:: ts

    /**
 * This code was GENERATED using the solita package.
 * Please DO NOT EDIT THIS FILE, instead rerun solita to update it or write a wrapper to add functionality.
 *
 * See: https://github.com/metaplex-foundation/solita
 */

import * as beet from '@metaplex-foundation/beet';
export type ClaimPackArgs = {
  index: number;
};

/**
 * @category userTypes
 * @category generated
 */
export const claimPackArgsBeet = new beet.BeetArgsStruct<ClaimPackArgs>(
  [['index', beet.u32]],
  'ClaimPackArgs',
);


