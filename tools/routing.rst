tools/routing.ts
================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import { RealmInfo } from 'models/registry/api'

export function getRealmExplorerHost(realmInfo: RealmInfo | undefined) {
  return realmInfo?.symbol === 'MNGO'
    ? 'dao.mango.markets'
    : 'realms-explorer.com'
}


