packages/js/src/plugins/guestIdentity/plugin.ts
===============================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import { PublicKey } from '@solana/web3.js';
import { GuestIdentityDriver } from './GuestIdentityDriver';
import { Metaplex } from '@/Metaplex';
import { MetaplexPlugin } from '@/types';

/** @group Plugins */
export const guestIdentity = (publicKey?: PublicKey): MetaplexPlugin => ({
  install(metaplex: Metaplex) {
    metaplex.identity().setDriver(new GuestIdentityDriver(publicKey));
  },
});


