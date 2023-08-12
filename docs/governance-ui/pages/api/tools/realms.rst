pages/api/tools/realms.ts
=========================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import { getCertifiedRealmInfos } from '@models/registry/api'
import { getConnectionContext } from '@utils/connection'

export function getAllSplGovernanceProgramIds(cluster = 'mainnet') {
  return [
    ...new Set(
      getCertifiedRealmInfos(getConnectionContext(cluster)).map((info) =>
        info.programId.toBase58()
      )
    ),
  ]
}


