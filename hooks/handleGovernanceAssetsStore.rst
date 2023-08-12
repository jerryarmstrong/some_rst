hooks/handleGovernanceAssetsStore.ts
====================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import { useEffect } from 'react'
import useGovernanceAssetsStore from 'stores/useGovernanceAssetsStore'
import { useRealmQuery } from './queries/realm'
import { useRealmGovernancesQuery } from './queries/governance'
import useLegacyConnectionContext from './useLegacyConnectionContext'

export default function useHandleGovernanceAssetsStore() {
  const realm = useRealmQuery().data?.result

  const connection = useLegacyConnectionContext()

  const governancesArray = useRealmGovernancesQuery().data

  const { setGovernancesArray } = useGovernanceAssetsStore()

  useEffect(() => {
    if (realm && governancesArray) {
      setGovernancesArray(connection, realm, governancesArray)
    }
  }, [connection, governancesArray, realm, setGovernancesArray])
}


