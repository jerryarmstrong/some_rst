hooks/useRealmGovernance.ts
===========================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import { PublicKey } from '@solana/web3.js'

import useRealm from './useRealm'

/// Returns Governance for the given pk  from the current realm
export default function useRealmGovernance(governance: PublicKey) {
  const realm = useRealm()

  return realm.governances[governance.toBase58()]?.account
}


