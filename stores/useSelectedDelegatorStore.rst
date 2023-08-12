stores/useSelectedDelegatorStore.tsx
====================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: tsx

    import { PublicKey } from '@solana/web3.js'
import create from 'zustand'

type Store = {
  communityDelegator?: PublicKey
  councilDelegator?: PublicKey
  setCommunityDelegator: (x?: PublicKey) => void
  setCouncilDelegator: (x?: PublicKey) => void
}

export const useSelectedDelegatorStore = create<Store>((set, _get) => ({
  communityDelegator: undefined,
  councilDelegator: undefined,
  setCommunityDelegator: (x) => set({ communityDelegator: x }),
  setCouncilDelegator: (x) => set({ councilDelegator: x }),
}))


