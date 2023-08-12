src/utils/identity.ts
=====================

Last edited: 2022-10-10 15:06:28

Contents:

.. code-block:: ts

    import { keypairIdentity, MetaplexPlugin } from '@metaplex-foundation/js'
import { Keypair } from '@solana/web3.js'
import { strict as assert } from 'assert'

export function resolveIdentity(keypair?: Keypair): MetaplexPlugin {
  if (keypair != null) return keypairIdentity(keypair)

  // TODO(thlorenz): when no keypair is provided return a cartera identity plugin
  assert.fail('We do not support cartera identity yet')
}


