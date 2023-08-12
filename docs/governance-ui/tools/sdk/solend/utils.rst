tools/sdk/solend/utils.ts
=========================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import { PublicKey } from '@solana/web3.js'

import SolendConfiguration from './configuration'

export async function deriveObligationAddressFromWalletAndSeed(
  walletAddress: PublicKey
) {
  return PublicKey.createWithSeed(
    walletAddress,
    SolendConfiguration.createObligationConfiguration.seed,
    SolendConfiguration.programID
  )
}


