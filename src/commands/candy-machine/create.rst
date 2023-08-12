src/commands/candy-machine/create.ts
====================================

Last edited: 2022-10-10 15:06:28

Contents:

.. code-block:: ts

    import { Commitment, Connection } from '@solana/web3.js'
import { urlFromCluster } from '@/utils/connection'
import {
  CandyMachineCreateArgs,
  clusterWithLocalToSdkCluster,
  DevCluster,
} from '@/types'
import { Metaplex, MetaplexPlugin } from '@metaplex-foundation/js'
import { candyMachineCreate } from '@/actions/candy-machine'
import { logInfo } from '@/utils'

export async function cmdCandyMachineCreate(
  cluster: DevCluster,
  commitment: Commitment,
  identity: MetaplexPlugin,
  args: CandyMachineCreateArgs
) {
  const url = urlFromCluster(cluster)
  const connection = new Connection(url, commitment)

  const mx = Metaplex.make(connection, {
    cluster: clusterWithLocalToSdkCluster(cluster),
  }).use(identity)
  const candyMachine = await candyMachineCreate(mx, args)
  logInfo('Successfully created candy machine at', candyMachine.address)
  return candyMachine
}


