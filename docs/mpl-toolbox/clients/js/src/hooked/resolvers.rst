clients/js/src/hooked/resolvers.ts
==================================

Last edited: 2023-06-19 17:40:55

Contents:

.. code-block:: ts

    import { PublicKey } from '@metaplex-foundation/umi';

export const resolveExtendLutBytes = (
  context: any,
  accounts: any,
  args: { addresses: Array<PublicKey> },
  programId: any
): number => 32 * args.addresses.length;


