Strategies/protocols/everlend/useInitMining.ts
==============================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import { Connection, PublicKey, Transaction } from '@solana/web3.js'
import { prepareInititalizeMining } from '@everlend/general-pool'

const getInitMiningTx = async (
  walletPubKey: PublicKey,
  connection: Connection,
  rewardPool: PublicKey
): Promise<Transaction> => {
  const tx = new Transaction()
  if (!walletPubKey) return tx
  const { tx: initMiningTx } = await prepareInititalizeMining(
    { payerPublicKey: walletPubKey, connection },
    rewardPool
  )

  tx.add(initMiningTx)

  return tx
}

export { getInitMiningTx }


