token-vault/js/src/generated/types/MintEditionProxyArgs.ts
==========================================================

Last edited: 2022-10-11 23:41:10

Contents:

.. code-block:: ts

    /**
 * This code was GENERATED using the solita package.
 * Please DO NOT EDIT THIS FILE, instead rerun solita to update it or write a wrapper to add functionality.
 *
 * See: https://github.com/metaplex-foundation/solita
 */

import * as beet from '@metaplex-foundation/beet';
export type MintEditionProxyArgs = {
  edition: beet.bignum;
};

/**
 * @category userTypes
 * @category generated
 */
export const mintEditionProxyArgsBeet = new beet.BeetArgsStruct<MintEditionProxyArgs>(
  [['edition', beet.u64]],
  'MintEditionProxyArgs',
);


