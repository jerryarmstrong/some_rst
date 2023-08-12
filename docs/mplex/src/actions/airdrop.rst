src/actions/airdrop.ts
======================

Last edited: 2022-10-10 15:06:28

Contents:

.. code-block:: ts

    import { Connection, LAMPORTS_PER_SOL, PublicKey } from '@solana/web3.js'
import { tryAmman } from '@/utils/amman'

export async function airdrop(
  connection: Connection,
  publicKey: PublicKey,
  amount: number
) {
  let signatureResult
  let signature

  const amman = tryAmman()
  if (amman != null) {
    ;({ signature, signatureResult } = await amman.airdrop(
      connection,
      publicKey,
      amount
    ))
  } else {
    signature = await connection.requestAirdrop(
      publicKey,
      amount * LAMPORTS_PER_SOL
    )
    signatureResult = await connection.confirmTransaction(signature)
  }

  return { signature, signatureResult }
}


