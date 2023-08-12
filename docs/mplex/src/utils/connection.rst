src/utils/connection.ts
=======================

Last edited: 2022-10-10 15:06:28

Contents:

.. code-block:: ts

    import { clusterApiUrl, Connection } from '@solana/web3.js'
import { ClusterWithLocal } from '@/types'
const LOCALHOST = 'http://127.0.0.1:8899'

export type ConnectionWithInternals = Connection & {
  _rpcWebSocket: { close: () => Promise<void> }
}

export async function closeConnection(
  connection: Connection,
  forceExit: boolean = false
) {
  try {
    const conn: ConnectionWithInternals = connection as ConnectionWithInternals
    if (forceExit) {
      setTimeout(() => process.exit(0), 200)
    }
    await conn._rpcWebSocket.close()
  } catch (err) {}
}

export function urlFromCluster(cluster: ClusterWithLocal) {
  if (cluster === 'local') return LOCALHOST
  return clusterApiUrl(cluster)
}


