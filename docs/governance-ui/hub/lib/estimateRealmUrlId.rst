hub/lib/estimateRealmUrlId.ts
=============================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import type { PublicKey } from '@solana/web3.js';

import realms from 'public/realms/mainnet-beta.json';

export function estimateRealmUrlId(realm: PublicKey) {
  for (const jsonRealm of realms) {
    if (jsonRealm.realmId === realm.toBase58() && jsonRealm.symbol) {
      return jsonRealm.symbol;
    }
  }

  return realm.toBase58();
}


