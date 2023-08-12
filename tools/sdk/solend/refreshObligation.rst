tools/sdk/solend/refreshObligation.ts
=====================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import { PublicKey, TransactionInstruction } from '@solana/web3.js'
import { refreshObligationInstruction } from '@solendprotocol/solend-sdk'

import SolendConfiguration, { SupportedMintName } from './configuration'

import { deriveObligationAddressFromWalletAndSeed } from './utils'

// Would be nice if we could automatically detect which reserves needs to be refreshed
// based on the obligationOwner assets in solend
export async function refreshObligation({
  obligationOwner,
  mintNames,
}: {
  obligationOwner: PublicKey
  mintNames: SupportedMintName[]
}): Promise<TransactionInstruction> {
  const obligationAddress = await deriveObligationAddressFromWalletAndSeed(
    obligationOwner
  )

  const depositReserves = SolendConfiguration.getReserveOfGivenMints(mintNames)

  return refreshObligationInstruction(
    obligationAddress,
    // Both deposit reserves + borrow reserves parameters leads to the same data in instruction
    // they are concatenate
    depositReserves,
    [],
    SolendConfiguration.programID
  )
}


