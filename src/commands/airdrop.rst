src/commands/airdrop.ts
=======================

Last edited: 2022-10-10 15:06:28

Contents:

.. code-block:: ts

    import { Commitment, Connection } from '@solana/web3.js'
import { urlFromCluster } from '@/utils/connection'
import { logInfo } from '@/utils'
import { airdrop } from '@/actions/airdrop'
import { DevCluster } from '@/types'
import { asPublicKey } from '@/utils/pubkey'

export async function cmdAirdrop(
  cluster: DevCluster,
  commitment: Commitment,
  pubkeyStr: string,
  amount: number
) {
  const pubkey = asPublicKey(pubkeyStr)
  const url = urlFromCluster(cluster)
  const shortCluster = pubkeyStr.slice(0, 10)
  logInfo(`Dropping ${amount}SOL to ${shortCluster}... on ${cluster} (${url})`)

  const connection = new Connection(url, commitment)

  const res = await airdrop(connection, pubkey, amount)
  return { connection, res }
}


