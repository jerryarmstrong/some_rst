packages/js/src/plugins/identityModule/plugin.ts
================================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import { IdentityClient } from './IdentityClient';
import type { Metaplex } from '@/Metaplex';
import { MetaplexPlugin } from '@/types';

/** @group Plugins */
export const identityModule = (): MetaplexPlugin => ({
  install(metaplex: Metaplex) {
    const identityClient = new IdentityClient();
    metaplex.identity = () => identityClient;
  },
});

declare module '../../Metaplex' {
  interface Metaplex {
    identity(): IdentityClient;
  }
}


