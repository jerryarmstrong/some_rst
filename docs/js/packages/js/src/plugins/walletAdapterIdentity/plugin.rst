packages/js/src/plugins/walletAdapterIdentity/plugin.ts
=======================================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import {
  WalletAdapterIdentityDriver,
  WalletAdapter,
} from './WalletAdapterIdentityDriver';
import { Metaplex } from '@/Metaplex';
import { MetaplexPlugin } from '@/types';

export const walletAdapterIdentity = (
  walletAdapter: WalletAdapter
): MetaplexPlugin => ({
  install(metaplex: Metaplex) {
    metaplex
      .identity()
      .setDriver(new WalletAdapterIdentityDriver(walletAdapter));
  },
});


