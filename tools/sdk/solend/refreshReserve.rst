tools/sdk/solend/refreshReserve.ts
==================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import { TransactionInstruction } from '@solana/web3.js'
import { refreshReserveInstruction } from '@solendprotocol/solend-sdk'

import SolendConfiguration, { SupportedMintName } from './configuration'

export async function refreshReserve({
  mintName,
}: {
  mintName: SupportedMintName
}): Promise<TransactionInstruction> {
  const {
    reserve,
    pythOracle,
    switchboardFeedAddress,
  } = SolendConfiguration.getSupportedMintInformation(mintName)

  return refreshReserveInstruction(
    reserve,
    SolendConfiguration.programID,
    pythOracle,
    switchboardFeedAddress
  )
}


