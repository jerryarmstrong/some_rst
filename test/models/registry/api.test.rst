test/models/registry/api.test.ts
================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import { getCertifiedRealmInfo } from 'models/registry/api'
import { getConnectionContext } from 'utils/connection'
import realms from 'public/realms/mainnet-beta.json'

test('getCertifiedRealmInfo', async () => {
  const mango = realms.find(({ symbol }) => symbol === 'MNGO')!

  const realmInfo = await getCertifiedRealmInfo(
    mango.symbol,
    getConnectionContext('mainnet')
  )

  expect(realmInfo!.realmId.toBase58()).toEqual(mango.realmId)
})


