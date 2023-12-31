hooks/useHydrateStore.tsx
=========================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    import { useRouter } from 'next/router'
import { useEffect } from 'react'
import useWalletStore from '../stores/useWalletStore'
import useRealm from './useRealm'

export default function useHydrateStore() {
  const router = useRouter()
  const { symbol, cluster, pk } = router.query
  const { proposals } = useRealm()
  const selectedRealmMints = useWalletStore((s) => s.selectedRealm.mints)
  const { fetchRealmBySymbol, fetchProposal } = useWalletStore((s) => s.actions)
  //Small hack to prevent race conditions with cluster change until we remove connection from store and move it to global dep.
  const routeHasClusterInPath = router.asPath.includes('cluster')
  useEffect(() => {
    if ((routeHasClusterInPath && cluster) || !routeHasClusterInPath) {
      fetchRealmBySymbol(cluster as string, symbol as string)
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps -- TODO please fix, it can cause difficult bugs. You might wanna check out https://bobbyhadz.com/blog/react-hooks-exhaustive-deps for info. -@asktree
  }, [symbol, cluster])
  useEffect(() => {
    if (pk && Object.entries(selectedRealmMints).length > 0) {
      fetchProposal(pk)
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps -- TODO please fix, it can cause difficult bugs. You might wanna check out https://bobbyhadz.com/blog/react-hooks-exhaustive-deps for info. -@asktree
  }, [pk, selectedRealmMints, JSON.stringify(proposals)])
}


