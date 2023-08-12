packages/js/src/plugins/keypairIdentity/plugin.ts
=================================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import { Keypair } from '@solana/web3.js';
import { KeypairIdentityDriver } from './KeypairIdentityDriver';
import { Metaplex } from '@/Metaplex';
import { MetaplexPlugin } from '@/types';

export const keypairIdentity = (keypair: Keypair): MetaplexPlugin => ({
  install(metaplex: Metaplex) {
    metaplex.identity().setDriver(new KeypairIdentityDriver(keypair));
  },
});


